print("Please enter the amount of money to convert: ")
print("# of dollars: ")
dollars=int(input())
print("# of cents: ")
cents=int(input())
cents=cents+(dollars*100)
quarter=cents//25
q_remainder=cents%25
dime=q_remainder//10
d_remainder=q_remainder%10
nickel=d_remainder//5
n_remainder=d_remainder%5
penny=n_remainder

print("The coins are", quarter,"quarters,", dime,"dimes,", nickel,"nickels and", penny,"pennies")
