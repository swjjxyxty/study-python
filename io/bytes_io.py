from io import BytesIO

f = BytesIO()

f.write("中午".encode('UTF-8'))

print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe5\x8d\x88')
print(f.read())
f.seek(0)
print(f.read())
