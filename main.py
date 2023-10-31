#Adrian Pelaez
def main():
    menu_selec = 0
    while menu_selec != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menu_selec = input("Please enter an option: ")
        if menu_selec == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            new_password = encode(password)  # changed variable name to avoid confusion
        elif menu_selec == "2":
            print("The encoded password is", new_password, "and the original password is", decoder(new_password))
        elif menu_selec == "3":
            break

def encode(password):
    new_pass = ""
    for dig in password:
        if int(dig) < 7:
            new_pass += str(int(dig) + 3)
        else:
            new_pass += str(int(dig) - 7)
    return new_pass


def decoder(password):
    pass_list = []
    # change each string character to int, then back to str, append to list
    for i in password:
        if int(i) < 3:
            pass_list.append(str(int(i) + 7)) # if digit is 2, then returns 12-3=9, not 2-3=-1
        else:
            pass_list.append(str(int(i) - 3))
    # change list to string without whitespace
    pass_string = "".join(pass_list)
    return pass_string


if __name__ == "__main__":
    main()