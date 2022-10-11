from urllib.request import urlopen
import ssl
import re

context = ssl._create_unverified_context()


with urlopen('https://stepik.org/media/attachments/lesson/209719/2.html', context=context) as webpage:
    content = webpage.read().decode('utf-8')

text = str(content)

tag = "code"

reg_str = "<" + tag + ">(.*?)</" + tag + ">"
res = re.findall(reg_str, text)

text = ''.join(res)

print(text.count('b'), text.count('c'))