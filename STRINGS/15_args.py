#sys module provides various functions and variables, used to manipulate different parts of the Python runtime environment.
#len(sys. argv) provides the number of command-line arguments.
#sys. argv[0] is the name of the current Python script.
import sys
x = len(sys.argv)
print("Total arguments passed:", x)
print("\nName of Python script:", sys.argv[0])
