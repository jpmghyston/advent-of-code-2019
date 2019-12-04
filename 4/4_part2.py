def password_is_valid(password):
    nums = [int(d) for d in str(password)]
    values = [0 for d in range(10)]
    values[nums[0]] += 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] < 0:
            return False
        values[nums[i]] += 1
    return 2 in values


valid_passwords = 0

for j in range(356261, 846303 + 1):
    if password_is_valid(j):
        valid_passwords += 1

print valid_passwords
