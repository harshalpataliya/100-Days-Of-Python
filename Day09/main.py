from art import logo
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} has the highest bid {highest_bid}")


bids={}
continue_bidding = True
while continue_bidding:
     name = input("Please enter your name: ").lower()
     price = int(input("Please enter your bid:$ "))
     bids[name] = price
     should_continue = input("Are there any new bidders? Type yes or no:\n")
     if should_continue == "no":
            continue_bidding = False
            find_highest_bidder(bids)
     elif should_continue == "yes":
            print("\n" * 80)
