'''
  Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise
   they need to put down 20%.
  Print the down payment.
'''
price_of_house = 1000000
good_credit = int(input('The total assets the buyer has:'))
down_10_percent = 0.1*1000000
doen_20_percent = 0.2*1000000
if good_credit:
    print(f"The total down payment after 10% is {price_of_house -down_10_percent}")
else:
    print(f"The total down payment after 20% is {price_of_house -down_20_percent}")

