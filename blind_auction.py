import art
print (art.logo)

def calculate_winner(bidding_record):
    winner= ""
    top_bid=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>top_bid:
            top_bid=bid_amount
            winner=bidder

    print("The winner is", winner,"who bid $",top_bid)

bids={}
cont_auction =True
while cont_auction == True:
    name =(input("What is your name: \n")).lower()
    bid=int(input("How much would you like to bid?:\n"))
    bids[name]=bid
    more_bidders=(input("Do more people want to bid? Type Yes or No \n")).lower()
    if more_bidders=="no":
        cont_auction=False
        print("Thank you. Stay tuned to find out the winner.")
        (calculate_winner(bids))
    elif more_bidders == "yes":
            print("\n" * 100)




# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


