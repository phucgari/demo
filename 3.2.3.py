a= ["banana","orange","apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total=0
def compute_bill(food):
    global total
    number=int(input("how many {0} do you want".format(food)))
    if stock[food]>0 and number<=stock[food]:
        total+=prices[food]*number
        print("total:",total)
        stock[food]-=number
    else:
        print("we dont have enough {0} for you".format(food))
        print("total:",total)
compute_bill("banana")
compute_bill("apple")
compute_bill("orange")
