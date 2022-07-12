def user_input():
    stop = "0"
    num = str(input("Enter a value: "))
    if num == " ":
        return float(stop)
    else:
        return float(num) + user_input()


def main_function():
    total = user_input()
    print("The Total of all the Values is ", total)


main_function()
