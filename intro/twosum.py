import os

def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        input()
        os.system('clear')
        for j in range(i + 1, n):
            print(f"i: {arr[i]} | j: {arr[j]}")
            if arr[i] + arr[j] == target:
                print(f"{arr[i]} + {arr[j]} = {arr[i] + arr[j]}")
                return True
    return False



def twoProd(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            print(f"i: {arr[i]} | j: {arr[j]}")
            if arr[i] * arr[j] == target:
                print(f"{arr[i]} x {arr[j]} = {arr[i] * arr[j]}")
                return True
    return False

if __name__ == '__main__':
    # arr = [0, -1, -2, -3]
    # target = -2

    arr = [4, 5, 2, 12, 6, 13, 15, 1, 8]
    target = 28

    if twoSum(arr, target):
        print("True")
    else:
        print("False")

    # if twoProd(arr, target):
    #     print("True")
    # else:
    #     print("False")

