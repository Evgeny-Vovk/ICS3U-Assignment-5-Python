# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: november 2022
# ICS3U-Assignment5.py File.


def main():

    # input and variables
    counter = 1
    prettier_counter = 0
    answer = 0

    # process and output
    print("")
    print("All the natural numbers that are multiples of 5 and 3, that are less than 1000 are:\n")
    while counter < 1000:
        if counter % 3 == 0 or counter % 5 == 0:
            print("{0} ".format(counter), end="")
            answer += counter
            prettier_counter += 1
            if prettier_counter % 10 == 0:
                print("")
        counter += 1
    print("\n\nThe sum of all these numbers is {}".format(answer))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
