
file = open("filepath", 'r')
#word = word that we want find
#text = file.read() #it give me like a unique string so we aren't use it

for line in file:
    if "word" in line:
        print(line.strip())

file.close()