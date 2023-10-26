#Adrian Pelaez
def main():
    menu_selec = 0
    while menu_selec != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menu_selec = input("Please enter an option: ")
        if menu_selec == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            password = encode(password)

def encode(password):
    new_pass = ""
    for dig in password:
        if int(dig) < 7:
            new_pass += str(int(dig) + 3)
        else:
            new_pass += str(int(dig) - 7)
    return new_pass


if __name__ == "__main__":
    main()