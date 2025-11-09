def find(s, n):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == n:
                return [i, j]
    return None


print("Enter the array:")
input_string = input()
nums_str = input_string.split()
nums = []
for x in nums_str:
    nums.append(int(x))

print("Enter the target value:")
target = int(input())

result = find(nums, target)

if result:
    print("Output: " , result)
else:
    print("No two numbers found that add up to the target")
