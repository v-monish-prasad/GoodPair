def goodPair(array, target):
    if not array:
        return "Array is empty"

    length = len(array)
    differences = set()

    for i in range(length):
        if target - array[i] in differences:
            return 1
        else:
            differences.add(array[i])

    return 0


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    target = int(input())
    print(goodPair(array, target))
