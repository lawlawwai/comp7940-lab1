def main():
    print("Hello World")
    # Find the all factors of x using a loop and the operator %
    # % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
    x = 52633
    for i in range(x + 1):
        if i == 0:
            continue
        if x % i == 0:
            continue

    # Write a function that prints all factors of the given parameter x
    def print_factor(x):
        for i in range(x + 1):
            if i == 0:
                continue
            if x % i == 0:
                print(i)

    # Write a program that be able to find all factors of the numbers in the list l
    l = [52633, 8137, 1024, 999]
    for number in l:
        print_factor(number)


if __name__ == '__main__':
    main()


    def reverse(string):
        string = string[::-1]
        return string

    print(reverse("test123"))