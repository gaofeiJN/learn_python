import ftplib
import os
import logging
from typing import List, Optional, Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FTPClient:
    def __init__(self, host: str, port: int = 21, user: str = '', password: str = '', passive: bool = True):
        """初始化FTP客户端"""
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.passive = passive
        self.ftp = None
    
    def connect(self) -> bool:
        """连接到FTP服务器"""
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(self.host, self.port, timeout=30)
            logger.info(f"Connected to {self.host}:{self.port}")
            
            if self.user:
                self.ftp.login(self.user, self.password)
                logger.info(f"Logged in as {self.user}")
            else:
                self.ftp.login()
                logger.info("Logged in anonymously")
            
            if self.passive:
                self.ftp.set_pasv(True)
                logger.info("Passive mode enabled")
            
            # 处理ZOS特定设置
            self._handle_zos_specifics()
            
            return True
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            return False
    
    def _handle_zos_specifics(self):
        """处理ZOS特定的FTP行为"""
        try:
            # 尝试设置二进制模式
            self.ftp.sendcmd('TYPE I')
            logger.info("Set binary mode")
        except Exception as e:
            logger.warning(f"Could not set binary mode: {e}")
    
    def disconnect(self):
        """断开FTP连接"""
        if self.ftp:
            try:
                self.ftp.quit()
                logger.info("Disconnected from server")
            except Exception as e:
                logger.error(f"Error disconnecting: {e}")
            finally:
                self.ftp = None
    
    def upload_file(self, local_path: str, remote_path: str) -> bool:
        """上传文件到服务器"""
        if not self.ftp:
            logger.error("Not connected to server")
            return False
        
        try:
            with open(local_path, 'rb') as f:
                self.ftp.storbinary(f'STOR {remote_path}', f)
            logger.info(f"Uploaded {local_path} to {remote_path}")
            return True
        except Exception as e:
            logger.error(f"Upload failed: {e}")
            return False
    
    def download_file(self, remote_path: str, local_path: str) -> bool:
        """从服务器下载文件"""
        if not self.ftp:
            logger.error("Not connected to server")
            return False
        
        try:
            # 确保本地目录存在
            local_dir = os.path.dirname(local_path)
            if local_dir and not os.path.exists(local_dir):
                os.makedirs(local_dir)
            
            with open(local_path, 'wb') as f:
                self.ftp.retrbinary(f'RETR {remote_path}', f.write)
            logger.info(f"Downloaded {remote_path} to {local_path}")
            return True
        except Exception as e:
            logger.error(f"Download failed: {e}")
            return False
    
    def list_files(self, remote_path: str = '.') -> List[str]:
        """列出服务器目录内容"""
        if not self.ftp:
            logger.error("Not connected to server")
            return []
        
        try:
            files = []
            self.ftp.dir(remote_path, lambda line: files.append(line))
            logger.info(f"Listed files in {remote_path}")
            return files
        except Exception as e:
            logger.error(f"List files failed: {e}")
            return []
    
    def change_directory(self, remote_path: str) -> bool:
        """更改服务器目录"""
        if not self.ftp:
            logger.error("Not connected to server")
            return False
        
        try:
            self.ftp.cwd(remote_path)
            logger.info(f"Changed directory to {remote_path}")
            return True
        except Exception as e:
            logger.error(f"Change directory failed: {e}")
            return False
    
    def get_current_directory(self) -> Optional[str]:
        """获取当前服务器目录"""
        if not self.ftp:
            logger.error("Not connected to server")
            return None
        
        try:
            return self.ftp.pwd()
        except Exception as e:
            logger.error(f"Get current directory failed: {e}")
            return None
    
    def __enter__(self):
        """上下文管理器入口"""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.disconnect()
