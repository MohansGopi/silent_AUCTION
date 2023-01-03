################### silent bidding auction ###################
###################### by - payakan ######################
from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\



'''

print(logo)

bidding = {}


def bid_conten():
  name = input("Enter Your Name : ")
  #bidding['name'] = name
  bid_ammount = int(input('Enter The Bidding Ammount $'))
  bidding[name] = bid_ammount


while True:
  bid_conten()
  bidder_here = input('If there any body want to bid, type yes or no :\n')
  bidder_here = bidder_here.lower()
  if bidder_here == 'yes':
    clear()
  elif bidder_here == 'no':
    clear()
    break
  else:
    print('you enter the wrong key')
    exit()
    

min = 0
for bidders in bidding:

  num = bidding[bidders]
  if num > min:
    max = num
    min = 0
    min += num
    bidding_person = bidders
  else:
    # print(min)
    max = min

print(f"The product sold to {bidding_person}, he's bidding ammount is ${max}")
