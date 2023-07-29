from art import logo

list_of_bidders = []
list_of_bids = []

def append_lists():
    """Asks user for names and bids. Adds these to list of bidders and list of bids."""
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    if bid.isdigit():
        list_of_bidders.append(name)
        list_of_bids.append(bid)
        return list_of_bidders, list_of_bids
    else:
        return False


def find_max_bid():
    """Finds the highest bid and name of the winner."""
    max_bid = max(bids)
    max_bid_index = bids.index(max_bid)
    winner = bidders[max_bid_index]
    print(f"The winner is {winner} with ${max_bid}.")


print(logo)
print("Welcome to the secret auction!")
game_on = True
while game_on:
    appended_bids = append_lists()
    if appended_bids:
        bidders, bids = appended_bids
        cont = input("Are there any other bidders? Type yes or no: ").lower()
        if cont == "no":
            find_max_bid()
            game_on = False
        elif cont == "yes":
            pass
        else:
            print("That answer is not valid.")
    else:
        print("That answer is not valid.")
