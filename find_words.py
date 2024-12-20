
file = open("C:/Users/saver/OneDrive/Desktop/file_python.txt", 'r')

#text = file.read() #it give me like a unique string

for line in file:
    if "pizza" in line:
        print(line.strip())

file.close()