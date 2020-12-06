smallest= None
for number in [9, 13, 5, 123, 67,89,3, 5353,34,53]:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    print(smallest,number)
