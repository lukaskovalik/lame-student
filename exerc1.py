def return_distinct(num1, num2, num3):
    number = [num1, num2, num3]
    if (num1 + num2 + num3) > 15:
        return max(number)
    elif (num1 + num2 + num3) < 10:
        return min(number)
    elif 10 < (num1 + num2 + num3) < 15:
        number.sort()
        return number[1]

x = return_distinct(1, 6, 5)
print(x)