# Python FTP Tool for ZOS

一个基于Python的命令行FTP工具，使用ftplib库实现与ZOS FTP服务器之间的文件上传和下载功能。

## 功能特性

- 连接到ZOS FTP服务器
- 上传文件到服务器
- 从服务器下载文件
- 列出服务器目录内容
- 支持配置文件管理
- 支持被动模式
- 处理ZOS特定的FTP行为

## 安装

1. 确保您已安装Python 3.7或更高版本
2. 克隆或下载此项目到本地
3. （可选）安装可选依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 基本语法

```bash
python cli.py --host <host> [--port <port>] [--user <user>] [--password <password>] --action <action> [--local <local>] [--remote <remote>]
```

### 命令行参数

- `--host`：FTP服务器地址（必填）
- `--port`：FTP服务器端口（默认：21）
- `--user`：用户名
- `--password`：密码
- `--action`：操作类型（必填，选项：upload/download/list）
- `--local`：本地文件/目录路径（上传和下载时必填）
- `--remote`：远程文件/目录路径（上传和下载时必填）
- `--passive`：使用被动模式（默认：True）
- `--config`：配置文件路径

### 示例

#### 上传文件

```bash
python cli.py --host ftp.example.com --user username --password password --action upload --local local_file.txt --remote remote_file.txt
```

#### 下载文件

```bash
python cli.py --host ftp.example.com --user username --password password --action download --local local_file.txt --remote remote_file.txt
```

#### 列出目录内容

```bash
python cli.py --host ftp.example.com --user username --password password --action list --remote /path/to/directory
```

## 配置文件

您可以创建配置文件来存储服务器信息，避免每次都输入相同的参数。

默认配置文件路径：`~/.ftptool/config.ini`

### 配置文件格式

```ini
[ftp]
host = ftp.example.com
port = 21
user = username
password = password
passive = true
```

## 注意事项

- 对于ZOS服务器，工具会自动设置二进制模式以确保文件传输的正确性
- 支持Windows、Linux和macOS平台
- 遇到连接问题时，请检查网络连接和服务器配置
- 对于大型文件传输，建议使用被动模式

## 错误处理

- 连接失败：会显示详细的错误信息
- 认证失败：会提示用户名或密码错误
- 文件传输失败：会显示具体的错误原因
- 网络超时：默认超时时间为30秒

## 扩展功能

- 未来计划支持SSH FTP（SFTP）
- 计划添加批量操作功能
- 计划支持文件压缩/解压
- 计划添加调度任务功能

## 贡献

欢迎提交问题和改进建议！

## 许可证

本项目采用MIT许可证。
