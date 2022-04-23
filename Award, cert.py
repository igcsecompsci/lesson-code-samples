print("RIAA awards certification to artists based on the number of albums, singles sold through retail and other ancillary markets")
NOU = input("Enter the number of units sold")
if NOU == 10000000:
    print("Diamond certified")
else:
    if NOU == 2000000:
        print("Multi Platinum certified")
    else:
        if NOU == 1000000:
            print("Platinum certified")
        else: 
            if NOU == 500000:
                print("Gold certified")
            else:
                print("Not eligible for certification")
            