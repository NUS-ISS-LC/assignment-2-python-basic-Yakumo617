def find(s, n):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == n:
                return [i, j]
    return None


print("Enter the array:")
nums = list(map(int, input().split()))

print("Enter the target value:")
target = int(input())

result = find(nums, target)

if result:
    print(f"Output: {result}")
else:
    print("No two numbers found that add up to the target")
