from urllib.request import urlopen
import ssl

context = ssl._create_unverified_context()

# with urlopen('https://stepik.org/media/attachments/lesson/209717/1.html', context=context) as webpage:
#     content = webpage.read().decode('utf-8')
with urlopen('https://ru.wikipedia.org/wiki/Python', context=context) as webpage:
    content = webpage.read().decode('utf-8')

print(content.count('C++'))
text = str(content)

ans = []

state = 0

for c in content:
    if c == '<':
        state += 1
    elif c == '>':
        state -= 1
    if state == 0:
        ans.append(c)

text = ''.join(ans)
print(content.count('C++'))