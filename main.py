print"number"
number=raw_input("enter a no n")
number=int(number)
if( number-1%4==0) or( number-2%4==0) or( number-3%4==0):
    print"s is winner"
else:
    print"p is winner"