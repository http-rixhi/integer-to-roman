# Program in python to take integer as input and convert it to Roman numerals.

class Solution():
    def intToRoman():

        num = int(input("num = "))

        print('"', end='')

        while num > 0:
            if num >= 1000:
                print("M", end="")
                num = num-1000

            elif num >= 900:
                print("CM", end="")
                num = num-900

            elif num >= 500:
                print("D", end="")
                num = num-500

            elif num >= 400:
                print("CD", end="")
                num = num-400

            elif num >= 100:
                print("C", end="")
                num = num-100

            elif num >= 90:
                print("XC", end="")
                num = num-90

            elif num >= 50:
                print("L", end="")
                num = num-50

            elif num >= 40:
                print("XL", end="")
                num = num-40

            elif num >= 10:
                print("X", end="")
                num = num-10

            elif num == 9:
                print("IX", end="")
                num = num-9
            
            elif num >= 5:
                print("V", end="")
                num = num-5

            elif num == 4:
                print("IV", end="")
                num = num-4
            
            elif num >= 1:
                print("I", end="")
                num = num-1

        print('"', end='')

    intToRoman()