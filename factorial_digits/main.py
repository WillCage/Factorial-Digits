import sys
import factorial_digits as fd

def main():
    user_input = sys.argv[1]

    if not user_input.isdigit():
        print("Please provide a non-negative integer.")
        exit()

    print(fd.calculate_sum_of_factorial_digits(int(user_input)))


if __name__ == '__main__':
    main()
