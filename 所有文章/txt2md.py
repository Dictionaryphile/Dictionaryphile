import os
import re
py_location = os.path.dirname(os.path.abspath(__file__))
print(py_location) # 打印当前 py 文件所在目录

os.chdir(py_location)
print(os.getcwd())

f = open(r'所有文章-按时间.txt', 'r', encoding='utf-8')

lines = f.read()
lines = re.sub(r'^(.+?)http(.+?)$', r'[\1](http\2)  ', lines, flags=re.MULTILINE)
f.close()

f = open(r'所有文章-按时间.md', 'w', encoding='utf-8')
f.write(lines)
f.close()
print('done!')
