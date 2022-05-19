# Author :- Biresashis Das

# In this program we will print the name of the person who bid the highest price.

print("-------- Welcome To The Bidding Game ---------\n")
new_dict = {}
should_continue = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_price = bidding_record[bidder]
    if bid_price > highest_bid:
      highest_bid = bid_price
      winner = bidder
  print(f"The Winner is {winner} with a bid of ${highest_bid}")

while should_continue:
    name = input("Enter your name : ")
    bid_price = int(input("Enter your Bid amount : $"))
    new_dict[name] = bid_price
    result = input("Is there are any other user. Type 'yes' for continue and 'no' for stop. ")

    if result == "yes":
        should_continue = True

    if result == "no":
        should_continue = False
        find_highest_bidder(new_dict)
        
        
        
        
