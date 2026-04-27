from ftplib import FTP

ftp = FTP("192.168.1.100")  # 连接FTP服务器
ftp.login("ibmuser", "sys1")  # 登录FTP服务器

# 列出目录内容
# print("-----dir()-----")
ftp.dir()  # 列出目录内容并打印到控制台

# print("-----nlst()-----")
nlist = ftp.nlst()  # 列出目录内容并返回一个列表
print(nlist)

# print("-----retrlines()-----")
ftp.retrlines("LIST")  # 列出目录内容并打印到控制台
ftp.retrlines("LIST 'IBMUSER.*'")  # 列出目录内容并打印到控制台
# ftp.retrlines("DIR")  # 500 unknown command DIR

# # 列出目录内容并写入文件
with open("host_file.txt", "w") as f:
    ftp.retrlines("LIST", lambda line: f.write(line + "\n"))


# 下载文件并写入本地文件
# # 一定要在HOST文件上使用单引号，否则会报550错误 # 550 RETR fails: /IBMUSER.COBOL.SRC(BKINQ) does not exist
with open("COBOL_SRC.TXT", "w") as f:
    ftp.retrlines("RETR 'IBMUSER.COBOL.SRC(BKINQ)'", lambda line: f.write(line + "\n"))

# 上传本地文件到FTP服务器
# 注意：命令前面不加QUOTE，否则会报500错误 # 500 unknown command QUOTE
print(ftp.sendcmd("SITE FILETYPE=SEQ"))  # 设置文件类型为顺序访问
print(ftp.sendcmd("SITE LRECL=80"))  # 设置记录长度为80
print(ftp.sendcmd("SITE RECFM=FB"))  # 设置记录格式为固定长度
print(ftp.sendcmd("SITE BLKSIZE=27920"))  # 设置块大小为27920
print(ftp.sendcmd("SITE UNIT=3390"))  # 设置设备类型为3390
print(ftp.sendcmd("SITE VOL=USR001"))  # 设置卷标为USR001
print(ftp.sendcmd("TYPE A"))  # 设置传输类型为ASCII

# 注意：虽然使用.storlines()方法上传文件，但是文件要以二进制模式打开"rb"
with open("host_file.txt", "rb") as f:
    ftp.storlines("STOR 'IBMUSER.HOST.FILES'", f)

ftp.quit()  # 退出FTP连接
