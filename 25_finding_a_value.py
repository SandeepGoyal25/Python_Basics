def is_group_member(group_data, n):
    group_data = [1, 5, 8, 3]
    for value in group_data:
        if n == 3:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 8))
# print(is_group_member([5, 8, 3], -2))