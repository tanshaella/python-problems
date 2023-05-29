print("Please enter the number of coins")
print("# of quarters")
quarters=int(input())
print("# of dimes")
dimes=int(input())
print("# of nickels")
nickels=int(input())
print("# of pennies")
pennies=int(input())
cent=25*quarters+10*dimes+5*nickels+1*pennies
dollars=cent//100
remainder=cent%100
print("The total is", dollars, "dollars", "and", remainder, "cents")
