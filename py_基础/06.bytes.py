# Python 3 中的字符串是 **Unicode 字符串**，内部采用**灵活字符串表示**（PEP 393）。根据字符串中最大 Unicode 码位的大小，选择以下三种固定宽度编码之一：

# - **Latin-1**（1 字节/字符）：如果所有码位 ≤ U+00FF。
# - **UCS-2**（2 字节/字符）：如果所有码位 ≤ U+FFFF（即基本多文种平面）。
# - **UCS-4**（4 字节/字符）：如果存在码位 > U+FFFF。

# 这种设计使得 Python 3 的字符串在内存使用上更高效，同时仍然能够支持全范围的 Unicode 字符。
# 对于大多数常见文本，Latin-1 或 UCS-2 就足够了，而只有包含较少使用的 Unicode 字符时才会使用 UCS-4。

# 字节串
print("----字节串---")
print(type(b"hello world"))  # <class 'bytes'>
print(isinstance(b"hello world", bytes))  # True

print(b"hello world")
print(b"hello world".decode("utf-8"))  # 将字节串解码为字符串
print("hello world".encode("utf-8"))  # 将字符串编码为字节串

print("中文".encode("utf-8"))  # 将字符串编码为字节串 # b'\xe4\xb8\xad\xe6\x96\x87'
print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))  # 将字节串解码为字符串 # "中文"

b = bytes("中文", "utf-16")  # 将字符串编码为字节串
print(b)  # b'\xff\xfe-N\x87e'
