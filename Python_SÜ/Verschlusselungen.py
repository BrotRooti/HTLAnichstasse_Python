'''
verschlüsselungs function
Phillip
28.03.22
'''
text = []

def cypher (txt):
    out = []
    for line in text:
        result = ""
        for x in range(len(line)-1,-1,-1):
            result = result+ line[x]
        out.append(result)
    return (out)

### main programm
print("Please input your text or 'end' to stop ->")
while(True):
    t = input()
    if (t == 'end'):
        break
    else:
        text.append(t)
output = cypher(text)
print(output)