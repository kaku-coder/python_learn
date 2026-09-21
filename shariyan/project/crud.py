content = "Python is easy to learn File handling is important I am practicing Python code"

with open("sample.txt",'w') as f:
    f.write(content)
    print(f)

with open ("sample.txt",'r') as f:
    read = f.read()
    print(read)

with open("sample.txt",'r')as f:
    index = f.read()
    print(index.find("f this is ${important}"))
    print("important" in read)
    
with open("sample.txt",'w') as f:
    replace_text = f.replace("python","java")
    print(replace_text)