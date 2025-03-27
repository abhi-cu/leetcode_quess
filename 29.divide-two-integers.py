def divide(dividend, divisor):
    if dividend == 0:
        return 0
    
    negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    
    if negative:
        quotient = -quotient
    
    return max(min(quotient, 2**31 - 1), -2**31)

dividend = 10
divisor = 3
print(divide(dividend, divisor)) 
