string = input('Input what you want. I will convert to float type: ')
try:
    print(float(string))
except ValueError:
    print("Yeah, I knew it. String can't be converted to float")
