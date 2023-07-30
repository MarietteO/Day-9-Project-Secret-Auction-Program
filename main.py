from art import logo

bidding_dict = {}


def ask_info():
    name = input("What is your name? ")
    bid = input("What is your bid? (Please enter a whole number, no cents): $ ")
    test = bid.isdigit()
    if test:
        bid = int(bid)
        bidding_dict[name] = bid
        return bidding_dict
    else:
        print("That answer is not valid. Please try again.")
        return False


def next_bidder():
    while True:
        cont = input("Is there another bidder? Type 'y' or 'n': ").lower()
        if cont == "y":
            return "y"
        elif cont == "n":
            return "n"
        else:
            print("That answer is not valid. Please try again.")


def get_winner(foo):
    return max(foo, key=foo.get)


def get_winning_bid(foo):
    return max(foo.values())


print(logo)
print("Welcome to the secret auction!")

game = True
while game is True:
    if ask_info():
        if next_bidder() == "n":
            break
print(f"The winner is {get_winner(bidding_dict)}, with ${get_winning_bid(bidding_dict)}.")
