n, m = map(int, input().split())
f = list(map(int, input().split()))

f.sort()

min_diff = float('inf')

for i in range(m - n + 1):
    diff = f[i + n - 1] - f[i]
    min_diff = min(min_diff, diff)

print(min_diff)
