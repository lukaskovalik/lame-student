numbers = [11, 202, 500, 6547, 1001]

def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += i
    return count

print(count_even(numbers))
