import main

text = ''

with open('test1.json','r') as f:
    lines = f.readlines()
    for l in lines:
        l = l.strip()
        text += l

res, error = main.run('<file>', text)

if error:
    print(error.as_string())
else:
    print(res)

# print(res)