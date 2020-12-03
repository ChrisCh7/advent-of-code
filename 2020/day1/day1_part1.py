def main():
    with open('in.txt') as input:
        lines = input.readlines()
        for line1 in lines:
            for line2 in lines:
                number1 = int(line1)
                number2 = int(line2)
                if number1 + number2 == 2020:
                    print('numbers: ' + str(number1) + ' ' + str(number2))
                    print('answer: ' + str(number1 * number2))
                    return


if __name__ == "__main__":
    main()
