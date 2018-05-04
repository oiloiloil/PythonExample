# 使用eval()計算輸入的算式
import re

print('Type quit to exit')
previous = 0
run = True

def performMath():
  global run # 為了讓performMath這個區塊裡面是吃到全域的run
  global previous
  equation = input('Enter Equation:')
  if(equation == 'quit'):
    run = False
  else:
    equation = re.sub('[a-zA-Z,.:()" "]', '', equation) #  避免user輸入python語法，出現不可預期的情形
    previous = eval(equation)
    print('Your equation is:', previous)

while run:
  performMath()
