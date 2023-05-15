


#---------------------------------------------------
#---------Membership Operator--------
#---------------------------------------------------
# in
# not in
#---------------------------------------

# String

name = "Salar"
print("S" in name) # True
print("a" in name) # True
print("A" in name) # False


print("#" * 50) # ##################################################

# List

friends = ["Salar" , "Abo Abass" , "Abo Saed" ]
print("Salar" in friends) # True
print("Abo Abass" not in friends) # False


print("#" * 50) # ##################################################


# Using In and Not in with if Condition

countriesOne = ["Deutschland" , "Egypt" , "Kuwait" , "Bahrain"]
countriesOneDiscount = 80

countriesTwo = ["Italy" , "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

# if myCountry == "Deutschland" or myCountry == "Egypt" or myCountry == "Kuwait" :
if myCountry in countriesOne :
    print(f"Hello You Have a Discount Equal To $ {countriesOneDiscount}") # Hello You Have a Discount Equal To $ 80

# elif myCountry == "USA" or myCountry == "Italy" :
elif myCountry in countriesTwo:
    print(f"You Have A Discaount Equal To $ {countriesTwoDiscount} ") # You Have A Discaount Equal To $ 50

else :
    print("You Have no Discount") # You Have no Discount











