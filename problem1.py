#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os, math
os.system('cls')

def start():
  print("Enter in the coefficients for a quadratic equation in the format:\n  ax^2 + bx + c = 0")
  while True:
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    try:
      a = int(a)
      b = int(b)
      c = int(c)
      break
    except:
      print("Those are not valid values for a, b or c")
  return a, b, c

def quadratic(a,b,c):
  try:
    x1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    print(f"The roots are {round(x1,2)} and {round(x2,2)}")
  except:
    print("There are no real roots to the equation")

if __name__ == "__main__":
  while True:
    a, b, c = start()
    quadratic(a, b, c)
