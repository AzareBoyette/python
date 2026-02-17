# Azare Boyette
# 2/17/2026
# P1HW2
# I will be making a program that takes information to make a budget to see how much would be needed to go on a trip
from decimal import Decimal
print("Hello please input name:")
user = input()
print("put in budget", user)
budget = Decimal(input())
print("Please put in travel distance", user)
distance = input()
try:
    distance = Decimal(distance)
except:
    print("You put:", distance)
    distance = None
print("How much do you think you will spend on gas", user)
gas = Decimal(input())
print("Around how much will you spend on accomodation/hotel", user)
accomodation = Decimal(input())
print("How much will you spend on food", user)
food = Decimal(input())

print("How much it will cost", user)
print("Your starting budget" ,user,"is", budget)
print("Gas cost", gas)
print("Accomodation cost", accomodation)
print("Food cost", food)
remaining = budget - gas - food - accomodation
print("Remaining left over.", remaining)