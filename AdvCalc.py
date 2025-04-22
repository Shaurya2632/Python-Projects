
from fractions import Fraction

class AdvCalc:

    @staticmethod
    def isArmstrong(num):
        validator = 0
        l = len(str(num))
        Original_num = num

        while num > 0:
            validator += pow(num % 10, l)
            num //= 10

        return validator == Original_num

    @staticmethod
    def Fibonacci_Series(*n):

        try:
           n = list(n)
           Fib = []

           if len(n) == 1:

               n = int(n[0])
               Fib = [0, 1]
               if int(n) < 2: return Fib[:n]

           elif len(n) == 2:

               for i in range(2):
                   if isinstance(n[i],list): n[i] = sum(n[i])

               Fib = [n[0], n[0] + 1]

               if n[1] - n[0] < 3: return Fib[:n]

               n = int(n[1])

           while (next_Fib := Fib[- 1] + Fib[- 2]) <= n:
                    Fib.append(next_Fib)

           return Fib

        except Exception as e:
            print(e)

    @staticmethod
    def Root(num, n):
        return pow(num, pow(n, -1))

    @staticmethod
    def AVG(nums):
        return sum(nums) / len(nums)

    @staticmethod
    def Exponent(num):

        for i in range(2, num):
            for j in range(2, num ** 2 + 2):
                if pow(i, j) == num:
                    return f"{i} ^ {j}"
                elif pow(i, j) > num: break

        return f"{num} ^ 1"

    @staticmethod
    def Divisor(n):
        divisors = []

        for i in range(1, n+1):
            if n % i == 0: divisors.append(i)

        return divisors

    @staticmethod
    def Probability(Favorable_outcomes, Total_outcomes):
        return Fraction(Favorable_outcomes/Total_outcomes).limit_denominator()

print(AdvCalc.Probability(5, 10000))
