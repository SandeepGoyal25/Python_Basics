# L1 = [3, 9, 4, 83, 64, 494, 93, 4, 2993, 4083, 404, 94, 14, 43, 45]
# print(L1.count(4))

def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count

print(list_count_4([7, 37, 4, 93, 4, 43, 8334, 4, 14]))