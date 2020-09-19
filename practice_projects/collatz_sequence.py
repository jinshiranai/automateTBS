import time

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = number * 3 + 1
        print(number)
        return number

def collatz_sequence():
    try:
        value = int(input("\nEnter your number: "))
    except ValueError:
        print("You must enter an integer.")
        collatz_sequence()
    else:
        sequence_step = collatz(value)

        while sequence_step != 1:
            sequence_step = collatz(sequence_step)
            time.sleep(0.5)

        print("We have arrived at the inevitable.")


collatz_sequence()