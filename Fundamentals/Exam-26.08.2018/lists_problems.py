data = input()

while data != 'stop playing':
    nums_list = list(map(int, data.split()))
    nums_set = set(nums_list)

    result = None
    
    if len(nums_list) == len(nums_set):
        result = [num + 2 if num % 2 == 0 else num for  num in nums_list]
        print(f"Unique list: {','.join(map(str, sorted(result)))}")
    else:
        result = [num + 3 if num % 2 == 1 else num for num in nums_list]
        print(f"Non-unique list: {':'.join(map(str, sorted(result)))}")

    print(f"Output: {sum(result) / len(result):.2f}")
    
    data = input()