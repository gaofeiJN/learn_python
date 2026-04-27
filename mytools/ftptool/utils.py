import os
import sys
from typing import Optional

def ensure_directory(path: str):
    """确保目录存在"""
    if not os.path.exists(path):
        os.makedirs(path)

def get_file_size(path: str) -> int:
    """获取文件大小"""
    try:
        return os.path.getsize(path)
    except Exception:
        return 0

def format_size(size: int) -> str:
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"

def validate_local_path(path: str) -> bool:
    """验证本地路径"""
    if not path:
        return False
    
    # 对于上传操作，检查文件是否存在
    if os.path.isfile(path):
        return os.path.exists(path)
    
    # 对于下载操作，检查目录是否存在
    dir_path = os.path.dirname(path) if os.path.isfile(path) else path
    if dir_path and not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
            return True
        except Exception:
            return False
    
    return True

def sanitize_remote_path(path: str) -> str:
    """清理远程路径"""
    if not path:
        return '.'
    
    # 确保路径使用正斜杠
    path = path.replace('\\', '/')
    
    # 移除末尾的斜杠
    if path.endswith('/'):
        path = path[:-1]
    
    return path

def get_filename_from_path(path: str) -> str:
    """从路径中获取文件名"""
    return os.path.basename(path)

def get_directory_from_path(path: str) -> str:
    """从路径中获取目录"""
    return os.path.dirname(path)
