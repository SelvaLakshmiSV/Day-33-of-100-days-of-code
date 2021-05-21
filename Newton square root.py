def newtonSqrt(n):
    approx_value = 0.5 * n
    better_value = 0.5 * (approx_value  + n/approx_value )
    while better_value != approx_value :
        approx_value = better_value
        better_value = 0.5 * (approx_value  + n/approx_value )
    return approx_value

print('The square root is' ,newtonSqrt(121)) 
