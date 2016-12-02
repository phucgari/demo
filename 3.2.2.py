a={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
b={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total=0
for key,value in a.items():
    print(key,value)
    price=value*b[key]
    total+=price
    print("total:",total)
