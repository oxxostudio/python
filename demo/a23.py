import re

# 取出一段文字中的阿拉伯數字
a = '123 + 456'
b = re.findall("\d+",a.replace(' ',''))  
print(b)

# 取出一段文字中的「非」阿拉伯數字
c = 'hello 123 !!!'
d = re.findall("\D+",c.replace(' ',''))
print(d)