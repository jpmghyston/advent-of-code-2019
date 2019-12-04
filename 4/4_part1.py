def password_is_valid(password):
    nums = [int(d) for d in str(password)]
    seen_two_sequential = False
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] < 0:
            return False
        if nums[i] - nums[i - 1] == 0:
            seen_two_sequential = True
    return seen_two_sequential


valid_passwords = 0

for j in range(356261, 846303 + 1):
    if password_is_valid(j):
        valid_passwords += 1

print valid_passwords

