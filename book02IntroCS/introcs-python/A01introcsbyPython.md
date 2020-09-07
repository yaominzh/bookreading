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

# chap04

Which features of the natural world are we studying? Inn most situations, we are interested in one fundamental characteristic: time.

We want to learn, through the scientific method, how to properly control the situation, just as when we launch a rocket, build a ridge, or smash an atom.

## scienfitic method
> the flllowing five-step approach briefly summarizes the scientific method:
- Observe some feature of the natural world.
- Hypothesize a model that is consistent with the observations
- Predict events using the hypothesis
- Verify the predictions by making further observations
- Validate by repeating until the hypothesis and observations agree.

One of the key tenets of the scientific method is that the experiments we design must be reproducible, so that others can convince themselves of the validity of the hypothesis.

## 4.1
python uses a much simpler internal representation for strings than for lists /arrays, a string ojbect contains: a reference to a place in memory + length of the string
## 4.1.1 3-sum problem
[code](threesum.py)
```python
import stdarray
import stdio
def writeTriples(a):
    pass

def countTriples(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) == 0:
                    count += 1
    return count
def main():
    a = stdarray.readInt1D()
    count = countTriples(a)
    stdio.writeln(count())
    if count<10:
        writeTriples(a)
if __name__ == '__main__': main()

```
## 4.2.x binary search
we start with lo = 0  and hi = n and the following recursive strategy:
- base case: if hi-lo equals 1, then the secret number is lo.
- recursive step: otherwise, ask whether the secret numbers is greater than or equal to the number mid = (hi + lo) // 2. if so, look for the number in [min, hi); if not, look for the number in [lo, mid).
```python
import sys
import stdio
def search(lo, hi):
    if (hi - lo) == 1:
        return lo
    mid = (hi + lo) // 2
    stdio.write('Greater than or equal to ' + str(mid) + '?')
    if stdio.readBool():
        return search(mid, hi)
    else:
        return search(lo, mid)
k = int(sys.argv[1])
n = 2**k
stdio.write('think of a number')
guess = search(0, n)
    


```