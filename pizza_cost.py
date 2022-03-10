#!/usr/bin/env python3
# Created by: Hunter Connolly
# March 10
# This program asks the user for the diameter of their pizza
# It the calculates the total cost of the pizza including tax

import constants


def main():
    # Get the diameter (Input)
    diameter = int(input("What is the diameter of your pizza? (inches): "))

    # Calculate the total price of the pizza (Process)
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST\
        + constants.INGRED_COST * diameter
    tax = subtotal * constants.HST
    total = subtotal + tax

    # display the total cost (output)
    print(" ")
    print("The total cost of the pizza is = ${:,.2f}" .format(total))


if __name__ == "__main__":
    main()
