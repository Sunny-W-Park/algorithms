#2947

import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
result = []

while True:
    sorted = True
    for i in range(4):
        a = arr[i]
        b = arr[i+1]
        if a > b:
            arr[i] = b
            arr[i+1] = a
            for j in range(5):
                print(arr[j], end = ' ')
            print()
    for i in range(4):
        if arr[i] > arr[i+1]:
            sorted = False
    if sorted == True:
        break

