
def isArmstrong(num):
  validator = 0
  l = len(str(num))
  Original_num = num
  
  while num > 0:
    validator += pow(num % 10, l)
    num //= 10
    
  return validator == Original_num
  
def Fibonacci_Series(n):
  Fib = [0,1]
  
  if n < 2: return Fib[:n]
  
  else: 
    for i in range(2, n + 1):
        
        next_Fib = Fib[i-1] + Fib[i-2]
      
        if next_Fib > n: break
        else: Fib.append(next_Fib)
          
    return Fib

def LCD(a, b):
  
   for i in range(max(a, b), a*b + 1, 1):
         if i % a == i % b == 0: return i
  
def GCD(a, b):
  
  return a * b // LCD(a, b)

