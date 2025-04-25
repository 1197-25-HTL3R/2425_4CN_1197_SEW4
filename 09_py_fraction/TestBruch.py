__author__ = 'Danijel Stamenkovic'

from Bruch import Bruch

if __name__ == '__main__':
    testcases = [
        Bruch(),
        Bruch(22,-13),
        Bruch(12,11)
    ]

    print()
    for bruch in testcases:
        print("  ", bruch)