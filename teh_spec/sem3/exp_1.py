def find_duplicates(nums):
    unique_nums = {}
    duplicates = []

    for num in nums:
        if num not in unique_nums:
            unique_nums[num] = True
        else:
            duplicates.append(num)

    return list(unique_nums.keys())

nums = [1, 2, 3, 1, 2, 4, 5, 1, 2, 3]
result = find_duplicates(nums)
print(result)  # [1, 2]