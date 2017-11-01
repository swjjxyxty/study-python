import os

print(os.name)

# windows 没有
# print(os.uname())

print(os.environ)

print(os.environ.get("PATH"))

print(os.environ.get("x", "default"))

# 查看当前目录
print(os.path.abspath("."))

# 创建目录
testDir = os.path.join('D:\\PycharmProjects\\study-python\\io', 'testdir')
os.mkdir(testDir)
assert os.path.exists(testDir)
os.rmdir(testDir)

# 分割目录
print(os.path.split('D:\\PycharmProjects\\study-python\\io\\test.txt'))
# 获取扩展名
print(os.path.splitext('D:\\PycharmProjects\\study-python\\io\\test.txt'))

# # 重命名
# os.rename("test.txt", "test.py")
# # 删除文件
# os.remove("test.py")

print([file for file in os.listdir(".") if os.path.isfile(file)])

print([file for file in os.listdir(".") if os.path.splitext(file)[1] == '.py'])
