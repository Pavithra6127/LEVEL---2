# LEVEL - 2

# TASK - 5 - File Manipulation

f = open("sample.txt", "r")
text = f.read()

words = text.split()
count = {}

for i in words:
    i = i.upper()
    
    if i in count:
        count[i] += 1
        
    else:
        count[i] = 1

for i in sorted(count):
    print(i, ":", count[i])


f.close()
