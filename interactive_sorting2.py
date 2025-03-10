import string


def interactive_sorting(alphabet,N,Q):
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if count >= Q :
                return 
            print(f'? {alphabet[i]} {alphabet[j]}')
            operator = input()
            count += 1
            if operator == '>':
                # Swap if the left weight is lighter
                alphabet[i], alphabet[j] = alphabet[j], alphabet[i]

def main():
    N, Q = map(int, input().split())
    alphabet = list(string.ascii_uppercase)

    alphabet = alphabet[:N]

    interactive_sorting(alphabet,N,Q)

    print(f"! {''.join(alphabet)}")

if __name__ == '__main__':
    main()