def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

numbers = [1, 3, 7, 2, 9, 4]
largest = find_largest(numbers)
print(f"The largest number in the list is: {largest}")