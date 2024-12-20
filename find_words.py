
file = open("C:/Users/saver/OneDrive/Desktop/file_python.txt", 'r')
#word = word that we want find
#text = file.read() #it give me like a unique string so we aren't use it

for line in file:
    if "word" in line:
        print(line.strip())

file.close()