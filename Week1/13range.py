def check_number_in_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False
number = int(input("Enter a number: "))
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

if check_number_in_range(number, start_range, end_range):
    print(f"{number} is within the range {start_range} to {end_range}.")
else:
    print(f"{number} is not within the range {start_range} to {end_range}.")