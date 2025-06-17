import sys
args = sys.argv[1:]
numbers = [int(arg) for arg in args]
print("Received parameters:", args)
print("Converted to numbers:", numbers)
print("Total numbers received:", len(numbers))
