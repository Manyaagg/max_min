# find_max_min.py

def find_max_min(numbers):
    if not numbers:
        return None, None # Return None if list is empty

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    return max_num, min_num

def main():
    data = [5, 2, 9, 1, 7, 3, 8]
    max_val, min_val = find_max_min(data)
    if max_val is not None:
        print(f"Numbers: {data}")
        print(f"Maximum number: {max_val}")
        print(f"Minimum number: {min_val}")
    else:
        print("List is empty, cannot find max/min.")

    empty_data = []
    max_val_empty, min_val_empty = find_max_min(empty_data)
    if max_val_empty is None:
        print(f"\nNumbers: {empty_data}")
        print("List is empty, cannot find max/min.")

if __name__ == "__main__":
    main()