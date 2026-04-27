import configparser
import os
from typing import Dict, Any

def load_config(config_path: str = None) -> Dict[str, Any]:
    """加载配置文件"""
    config = {}
    
    # 确定配置文件路径
    if config_path:
        if not os.path.exists(config_path):
            return config
    else:
        # 默认配置文件路径
        config_path = os.path.join(os.path.expanduser('~'), '.ftptool', 'config.ini')
        if not os.path.exists(config_path):
            return config
    
    # 加载配置文件
    try:
        parser = configparser.ConfigParser()
        parser.read(config_path)
        
        if 'ftp' in parser:
            ftp_section = parser['ftp']
            if 'host' in ftp_section:
                config['host'] = ftp_section['host']
            if 'port' in ftp_section:
                try:
                    config['port'] = int(ftp_section['port'])
                except ValueError:
                    pass
            if 'user' in ftp_section:
                config['user'] = ftp_section['user']
            if 'password' in ftp_section:
                config['password'] = ftp_section['password']
            if 'passive' in ftp_section:
                config['passive'] = ftp_section['passive'].lower() == 'true'
    
    except Exception as e:
        print(f"Error loading config file: {e}")
    
    return config

def create_default_config():
    """创建默认配置文件"""
    config_dir = os.path.join(os.path.expanduser('~'), '.ftptool')
    config_path = os.path.join(config_dir, 'config.ini')
    
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    
    if not os.path.exists(config_path):
        parser = configparser.ConfigParser()
        parser['ftp'] = {
            'host': '',
            'port': '21',
            'user': '',
            'password': '',
            'passive': 'true'
        }
        
        with open(config_path, 'w') as f:
            parser.write(f)
        
        print(f"Created default config file at {config_path}")
