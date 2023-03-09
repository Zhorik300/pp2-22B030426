import time   
num = int(input())  
milsec = int(input())  
sec = milsec/1000  
time.sleep(sec)  
sqrt = num ** 0.5  
txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum = num, fsec = milsec, fsqrt = sqrt)  
print(txt)  
  