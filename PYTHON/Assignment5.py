import os
with open("sample.txt",'w') as f:
    f.write("Hello welcome to python class")
with open("sample.txt",'a') as f:
    f.write("\nPython is a language which is easy to learn")
with open("sample.txt",'r') as f:
    content=f.read()
    print(content)
