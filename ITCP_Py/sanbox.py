def sqrt_long(x):
    epsilon = 1
    numGuess = 0
    # x = 25
    low = 1
    high = x
    ans = (high + low)//2
    while abs(ans**2 -x) >= epsilon and numGuess < x:
        print('x=', x,'low=', low, 'high=', high, 'ans=', ans)
        numGuess +=1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)//2
    print('numGuess = ', numGuess)
    print(ans, 'is close to square root of', x)
for i in range(1, 16):

    sqrt_long(i)
if __name__ == '__main__':
    pass