# Two pointer

n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
start = 0
end = 0
interval_sum = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)


# 정렬되어 있는 두 리스트의 합집합

n, m = 3, 4 #리스트 길이
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n+m)
idx_a = 0
idx_b = 0
k = 0

while idx_a < n or idx_b < m:
    if idx_b >= m or (idx_a < n and a[idx_a] <= b[idx_b]):
        result[k] = a[idx_a]
        idx_a += 1
    else:
        result[k] = b[idx_b]
        idx_b += 1
    k += 1

for i in result:
    print(i, end = ' ')

