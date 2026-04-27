import argparse
import sys
from ftpclient import FTPClient
from config import load_config

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='FTP client tool for ZOS servers')
    
    # 服务器连接参数
    parser.add_argument('--host', type=str, help='FTP server host')
    parser.add_argument('--port', type=int, default=21, help='FTP server port (default: 21)')
    parser.add_argument('--user', type=str, help='Username')
    parser.add_argument('--password', type=str, help='Password')
    parser.add_argument('--passive', action='store_true', default=True, help='Use passive mode (default: True)')
    
    # 操作参数
    parser.add_argument('--action', type=str, required=True, choices=['upload', 'download', 'list'],
                      help='Action to perform: upload, download, or list')
    parser.add_argument('--local', type=str, help='Local file/directory path')
    parser.add_argument('--remote', type=str, help='Remote file/directory path')
    
    # 配置文件参数
    parser.add_argument('--config', type=str, help='Configuration file path')
    
    return parser.parse_args()

def main():
    """主函数"""
    args = parse_arguments()
    
    # 加载配置
    config = load_config(args.config)
    
    # 使用命令行参数覆盖配置
    host = args.host or config.get('host')
    port = args.port or config.get('port', 21)
    user = args.user or config.get('user', '')
    password = args.password or config.get('password', '')
    passive = args.passive
    
    # 验证必要参数
    if not host:
        print('Error: --host is required')
        sys.exit(1)
    
    if args.action in ['upload', 'download']:
        if not args.local:
            print('Error: --local is required for upload/download')
            sys.exit(1)
        if not args.remote:
            print('Error: --remote is required for upload/download')
            sys.exit(1)
    
    # 创建FTP客户端
    client = FTPClient(host, port, user, password, passive)
    
    try:
        # 连接服务器
        if not client.connect():
            print('Error: Failed to connect to server')
            sys.exit(1)
        
        # 执行操作
        if args.action == 'upload':
            success = client.upload_file(args.local, args.remote)
            if success:
                print(f'Successfully uploaded {args.local} to {args.remote}')
            else:
                print(f'Failed to upload {args.local}')
                sys.exit(1)
        
        elif args.action == 'download':
            success = client.download_file(args.remote, args.local)
            if success:
                print(f'Successfully downloaded {args.remote} to {args.local}')
            else:
                print(f'Failed to download {args.remote}')
                sys.exit(1)
        
        elif args.action == 'list':
            remote_path = args.remote or '.'
            files = client.list_files(remote_path)
            if files:
                print(f'Files in {remote_path}:')
                for file in files:
                    print(file)
            else:
                print(f'Failed to list files in {remote_path}')
                sys.exit(1)
    
    finally:
        # 断开连接
        client.disconnect()

if __name__ == '__main__':
    main()
