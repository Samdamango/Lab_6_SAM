def encode(password_to_encode):
    for i in range(len(password_to_encode)):
        add_encode = int(password_to_encode[i]) + 3



if __name__ == '__main__':

    while True:
        print("\nMenu")
        print("-"*13)
        print("1.Encode\n2.Decode\n3.Quit\n")

        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            password_to_encode = str(input("Please enter your password to encode: "))
            encoded_password = encode(password_to_encode)
            #make encode function and encode it
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password_to_encode}")
        elif user_input == 3:
            break
