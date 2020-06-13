# For easier manual data spliting when hardcoding lists

split_val = input("Val to split: ")
print()
user_input = input("Enter String: ")
print()
while user_input != "exit":
    print(user_input.split(split_val))
    user_input = input("Enter String: ")
    print()
