def input_checker(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


total = 0

for i in range(0, 5):

    num_in = input("Enter int #{}: ".format(i + 1))

    while input_checker(num_in) is False:
        print("Invalid Input. Please enter an int.")
        num_in = input("Enter int #{}: ".format(i + 1))

    num_in = int(num_in)
    total += num_in

print("Your sum is: {}".format(total))
