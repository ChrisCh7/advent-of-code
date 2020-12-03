def main():
    with open('in.txt') as input:
        lines = input.readlines()
        for line1 in lines:
            for line2 in lines:
                for line3 in lines:
                    number1 = int(line1)
                    number2 = int(line2)
                    number3 = int(line3)
                    if number1 + number2 + number3 == 2020:
                        print('numbers: ' + str(number1) + ' ' + str(number2) + ' ' + str(number3))
                        print('answer: ' + str(number1 * number2 * number3))
                        return


if __name__ == "__main__":
    main()
