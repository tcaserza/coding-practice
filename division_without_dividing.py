def divide(dividend, divisor):
    if divisor > dividend:
        return 0
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient

print divide(25,2)