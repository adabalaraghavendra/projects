import os 
bids={}
bidding_finnish= False
def finding_highest_bidder(bid_record):
    highest_bid=0
    winner=""
    for bidder in bid_record:
        bid_ammount=bid_record[bidder]
        if bid_ammount> highest_bid:
            highest_bid=bid_ammount
            winner=bidder
    print(f"The winner is{winner} with bid of ${highest_bid}")

while not bidding_finnish:
    name=input("enter the name\n")
    bid=int(input("enter the bid ammount\n"))
    bids[name]=bid
    bidding=input("is any one want to bid type 'yes',for stop 'no'\n")
    if bidding=="yes":
        os.system('cls')
    elif bidding=="no":
        bidding_finnish= True
        finding_highest_bidder(bids)


