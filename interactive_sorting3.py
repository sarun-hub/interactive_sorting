import string

def partition(arr, low, high, count, Q):
    if count[0] >= Q:
        return low
    
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if count[0] >= Q:
            break

        print(f'? {arr[j]} {pivot}')
        operator = input().strip()
        count[0] += 1

        if operator == '<':  # arr[j] < pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, count, Q):
    if low < high and count[0] < Q:
        pi = partition(arr, low, high, count, Q)
        quicksort(arr, low, pi - 1, count, Q)
        quicksort(arr, pi + 1, high, count, Q)

def main():
    N, Q = map(int, input().split())
    alphabet = list(string.ascii_uppercase)[:N]

    count = [0]  # Use a list to keep count mutable
    quicksort(alphabet, 0, N - 1, count, Q)

    print(f"! {''.join(alphabet)}")

if __name__ == '__main__':
    main()
