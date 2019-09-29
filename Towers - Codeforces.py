#https://codeforces.com/problemset/problem/37/A
'''
Comment
'''

if __name__ == "__main__":
    n = int(input())
    bars = list(map(int, input().split()))

    bars.sort()
    total_number = 1
    current_hight = 1
    higth_tower = 1

    for i in range(n - 1):
        if bars[i] != bars[i + 1]:
            total_number += 1
            current_hight = 1
        else:
            current_hight += 1
            higth_tower = max(higth_tower, current_hight)

    print(higth_tower, total_number)
