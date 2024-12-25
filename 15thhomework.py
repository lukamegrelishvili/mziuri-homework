#first part of homework
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "error: can't divide on zero lil bro"
    except TypeError:
        return "error:type numbers not letters "

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))  
#second part of homework
my_list = [1, 2, 3, 4]

try:
    print(my_list[10])
except IndexError:
    print("error:this shi is out of list's range")

#third part of homework
    try:
        with open("myresult.txt", "r") as file:
            content = file.read()
            print("content of file:")
            print(content)
    except FileNotFoundError:
        print("error:there's no 'myresult.txt' file bro")

