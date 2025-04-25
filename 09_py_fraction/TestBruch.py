__author__ = 'Danijel Stamenkovic'

from Bruch import Bruch

if __name__ == '__main__':
    Bruch1 = Bruch()
    Bruch2 = Bruch(4,-7)
    Bruch3 = Bruch(5,6)

    print(f"{Bruch1.__str__()}\n{Bruch2.__str__()}\n{Bruch3.__str__()}")
    print(f"\n Calculations")
    print(f"Add:{Bruch2.__str__()} + {Bruch3.__str__()} = {Bruch2.add(Bruch3)}")
    print(f"Add:{Bruch2.__str__()} - {Bruch3.__str__()} = {Bruch2.sub(Bruch3)}")
    print(f"Add:{Bruch2.__str__()} * {Bruch3.__str__()} = {Bruch2.mult(Bruch3)}")
    print(f"Add:{Bruch2.__str__()} / {Bruch3.__str__()} = {Bruch2.div(Bruch3)}")

