print("包含中文的string")

# char to code : ord
print(ord("A"))
print(ord("中"))

# code to char : chr
print(chr(66))
print(chr(25991))

print("\u4e2d\u6578")

# bytes
byteStr = b'ABC'

print("ABC".encode("ascii"))

print("中午".encode("utf-8"))

print(byteStr.decode("ascii"))

print("中文".encode("utf-8").decode("utf-8"))

# len
# !/bin/bash/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
print(len("ABC"))
print(len("中文"))

print(len("中文".encode("utf-8")))

# string format

print("String = %s." % "string")
print("Integer = %d" % 100)
print("Integer = %2d-%02d" % (100, 1))
print("Float = %f" % 2.34)
print("Hex = %x" % 999)

print("Float = %.1f" % 2.34)
