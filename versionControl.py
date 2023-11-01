# Lab 6: Version Control | 10/31/23 | Brock Gilman


# encode function
def encode(password):
    encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded_password


def decode_password(encoded_password):
    original_password = ''.join(str((int(digit) - 3) % 10) for digit in encoded_password)
    return original_password


# main function
def main():
    # while loop to print menu
    while True:
        print(f"Menu\n"
              f"-------------\n"
              f"1. Encode\n"
              f"2. Decode\n"
              f"3. Quit\n")

        # menu_option input
        menu_option = input(f"Please enter an option: ")

        # if statement menu_option '1' (encode)
        if menu_option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored!")

        # elif statement menu_option '2' (decode)
        elif menu_option == "2":
            original_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")

        # elif statement menu_option '3' (quit)
        elif menu_option == "3":
            break

