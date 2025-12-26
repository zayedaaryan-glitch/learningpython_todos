feet_inches = input("Enter feet and inches: ")

from parsers import parse

from converters import convert

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f'{parsed["feet"]} feet and {parsed["inches"]} inches')

if result > 1:
    print("kid is safe to go")
else :
    print("kid is not safe to go")

