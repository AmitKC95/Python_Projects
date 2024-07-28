import sys

print(sys.executable)                  # Path to the Python interpreter executable.
print(sys.platform)                    # Platform identifier (e.g., 'win32', 'linux', 'darwin' for macOS).
print(sys.argv[0])                     # Name of the script being executed.
print(sys.version_info.major)          # Major version number of the Python interpreter.
print(sys.getsizeof(1))                # Memory size of the integer 1.
print(sys.getsizeof(42))               # Memory size of the integer 42.
print(sys.getsizeof(1.0))              # Memory size of the float 1.0.
print(sys.getsizeof(""))               # Memory size of an empty string.
print(sys.getsizeof("a"))              # Memory size of a string with one character.
print(sys.getsizeof("ab"))             # Memory size of a string with two characters.
print(sys.getsizeof("abcdefghij"))     # Memory size of a string with ten characters.

print("hello", end=" p")
print("world")

val = input("Type in a number: ")
print(val)
print(val.isdecimal())  # True if only decimal digits (0-9)
print(val.isnumeric())  # True if numeric (including decimals, fractions)

if val.isdecimal(): #2.5 and 2/5 are not valid
    num = int(val)
    print(num)

from fractions import Fraction

val = input("Type in a number: ")
print(val)

try:
    num = Fraction(val)
    print(num)
except ValueError:
    print("The input is not a valid number.")
