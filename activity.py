string = input("Enter a string: ") 
n = int(input("Enter a non negative: "))

def get_copies(string, n): 
    if n < 0: 
       return "number of copies "

    if len(string) < 2: 
       return string * n

    return string [:2] * n

print(get_copies(string, n))
