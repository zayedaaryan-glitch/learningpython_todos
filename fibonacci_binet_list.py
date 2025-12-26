from math import sqrt


def nth_fibonacci_binet(n):

    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2

    fn = (phi ** n - psi ** n) / sqrt(5)
    return int(round(fn))


n_list = []
while True:
    try:
        sequence_number = int(input("Please enter the sequence number: "))
        for x in range(0, sequence_number):
            n_list.append(nth_fibonacci_binet(x))

        for index, seq in enumerate(n_list):
            print(f"fibonacci number#{index+1}: {seq}")
        break
    except ValueError:
        print("Please enter a valid number.")
        continue

