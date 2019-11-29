# print(len("1073412207@qq.com"))
import re

# if re.match(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', "1073412207@qq.com"):
#     print('True')


idcode = '''
<div id="ehong-code" class="ehong-idcode-val ehong-idcode-val3" href="#" onblur="return false" onfocus="return false" oncontextmenu="return false" onclick="$.idcode.setCode()"><font color="#90719B">i</font><font color="#18975F">e</font><font color="#BF0C43">g</font><font color="#707F02">D</font></div><span id="ehong-code-tip-ck" class="ehong-code-val-tip" onclick="$.idcode.setCode()"></span>

'''
#
# print(idcode)
idcode = re.findall(r'<font color=(.*)</font>', idcode, flags=re.I)
print(idcode)
idcode1 = idcode[0].split('>')
print(idcode1)
str1 = ''
for i in [idcode1[1],idcode1[3], idcode1[5]]:
    str1 += i[0]
idcode = str1+ idcode1[-1]
print(idcode)