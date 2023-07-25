def manual_division(dividend, divisor):
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    quotient *= sign
    return quotient




# Example usage
result = manual_division(10, 3)
print(result)  # Output: 3