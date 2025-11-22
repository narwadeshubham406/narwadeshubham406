from logo import gavel
print(gavel)
print("Welcome to Govinda Enterprises. Enjoy the bidding !!!!!!!!!!!!!!!!")
bids ={}

def find_highest_bidder(bidding_dictonary):
    winner = ""
    higest_bid = 0

    for bidder in bidding_dictonary:
        bid_amount = bidding_dictonary[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of $ {higest_bid}")


continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("Please provide your bid amount in $: "))
    bids[name] = price
    bid_desire = input("Do you want to provide the bid 'YES' or 'NO': \n").lower()
    if bid_desire == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif bid_desire == "yes":
        print("\n" * 500)




