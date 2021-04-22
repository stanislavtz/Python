# def increase_even()
data = input()

while data != 'stop playing':
    nums_list = list(map(int, data.split()))

    nums_set = set(nums_list)

    if len(nums_list) == len(nums_set):
        unique = [num + 2 if num % 2 == 0 else num for  num in nums_list]
        print(f"Unique list: {','.join(map(str, sorted(unique)))}")
        print(f"Output: {sum(unique) / len(unique):.2f}")

    else:
        unique = [num + 3 if num % 2 == 1 else num for num in nums_list]
        print(f"Non-unique list: {':'.join(map(str, sorted(unique)))}")
        print(f"Output: {sum(unique) / len(unique):.2f}")

    data = input()