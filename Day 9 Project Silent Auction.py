import os
clear = lambda: os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.


print(logo)
game_status = True
auction = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${bid_amount}")

while game_status:
  bidder_name = input("What's your name?: ")
  bid_price = int(input("What's your bid?: $"))
  auction[bidder_name] = bid_price
  more_bidders = input("Are there any more bidder? yes or no \n").lower()
  if more_bidders == "yes":
    clear()
  elif more_bidders == "no":
    game_status = False
    find_highest_bidder(auction)
    
