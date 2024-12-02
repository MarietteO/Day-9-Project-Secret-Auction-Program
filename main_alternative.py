#Not as modular, but does the trick.

def user_bids():
    user_dictionary = {}
    game = True
    while game:
        name = input("What is your name? ")
        while True:
            bid = input("What is your bid? Please enter a whole number, no cents: R")
            if not bid.isdigit():
                print("That is not a valid answer.")
            else:
                user_dictionary[name] = int(bid)
                break
        cont = input("Would someone else like to place a bet? Type y for yes or anything else for n: ").lower()
        if cont != "y":
            game = False
    return user_dictionary


print("Welcome to the secret auction!")
new_dict = user_bids()
winning_bid = 0
winner = ""
for key in new_dict:
    if new_dict[key] > winning_bid:
        winning_bid = new_dict[key]
        winner = key
print(f"The winner is {winner} with R{winning_bid}.")
