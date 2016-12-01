a={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total=0
for key,value in a.items():
    print(key,value)
    print("price:",value)
    number=int(input(key))
    price=value*number
    total+=price
    print("total:",total)
