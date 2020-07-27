[[toc]]
# chap01 
## 1.1.2 useargument.py
```python
import sys
import stdio
stdio.write('Hi, ')
# stdio.write(sys.argv[1])
stdio.writeln('. How are you?')
```

## 1.2.5 leapyear.py
```python
import sys
import stdio
# year = int(sys.argv[1])
year = 2004
isLeapYear=(year%4==0)
isLeapYear=isLeapYear and((year % 100) != 0)
isLeapYear = isLeapYear or ((Year % 400) == 0)
stdio.writeln(isLeapYear)
```
## 1.3.6 Newton's method sqrt.py
```python
import sys
import stdio
EPSILON = 1e-15
# c = float(sys.argv[1])
c = float(25)
t = c
while abs(t-c/t) > (EPSILON * t):
    t = (c/t + t) / 2.0
stdio.writeln(t)
```
## 1.3.9 factoring integers 
factors.py
```python
import sys
import stdio
# n= int(sys.argv[1])
n= int(25)
factor = 2
while factor*factor <= n:
    while (n % factor) ==0:
        n //=factor
        stdio.write(str(factor) + ' ')
    factor +=1
if n>1:
    stdio.write(n)
stdio.writeln()
```
## 1.4
the essence of programming language design is a tradeoff between simplicity and efficiency.

## 1.4.1 samplingn without replacement
[code](sample.py)
```python
import random
import sys
import stdarray
import stdio

# m = int(sys.argv[1])
# n = int(sys.argv[2])
m = 4
n = 5
perm = stdarray.create1D(n,0)
print(perm)
for i in range(n):
    perm[i] = i

print(perm)
for i in range(m):
    r = random.randrange(i,n)
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp
for i in range(m):
    stdio.write(str(perm[i])+ ' ' )
stdio.writeln()
```
## 1.4.3 sieve of Eratosthenes
[code](primesieve.py)
## 