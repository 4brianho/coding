#---------------------------------------------------------sandwhich--------------------------------------------------------
msg="What type of sandwhich would you like?\na) Chicken Sandwhich-$5.25\nb) Beef Sandwhich-$6.25\nc) Tofu Sandwhich-$5.75\n"
selectedsandwhich = ""
beveragesize = ""
frenchfrysize = ""

sandwhichlist = ["a", "b", "c"]
total = 0.00
selectedsandwhich = (input(msg)).lower()
while selectedsandwhich not in sandwhichlist:
    selectedsandwhich = (input("Please select a, b, or c: ")).lower()
    
if selectedsandwhich == "a":
  print("You selected Chicken Sandwhich\nTotal: $5.25")
  total = 5.25
elif selectedsandwhich == "b":
  print("You selected Beef Sandwhich\nTotal: $6.25")
  total = 6.25
else:
  print("You selected Tofu Sandwhich\nTotal: $5.75")
  total = 5.75
#---------------------------------------------------------beverages--------------------------------------------------------
beverage = (input("Would you like a beverage? Yes/No: ")).lower()
choice = ["yes","no"]
while beverage.lower() not in choice:
  beverage = (input("Please answer yes or no: ")).lower()
  
if beverage == "yes":
  beveragesizelist = ["small", "medium","large"]
  beveragesize=(input("What size beverage would you like?\nsmall-$1.00\nmedium-$1.75\nlarge-$2.25\n")).lower()
  while beveragesize.lower() not in beveragesizelist:
    beveragesize = input("Please select small, medium or large: ").lower()
  if beveragesize =="small":
    total = total + 1
    print(f"You selected small\n\nYour current total is ${total:.2f}\n")
  elif beveragesize =="medium":
   total = total + 1.75
   print(f"You selected medium\n\nYour current total is ${total:.2f}\n")
  else:
    total = total + 2.25
    print(f"You selected large\n\nYour current total is ${total:.2f}\n")
#---------------------------------------------------------frenchfries------------------------------------------------------
frenchfrysizelist =["small","medium","large"]
frenchfries= (input("Would you like french fries? Yes/No: ")).lower()
while frenchfries not in choice:
  frenchfries = (input("Please answer yes or no: ")).lower()
  
if frenchfries == "yes":
  frenchfrysize =(input("What size french fries would you like?\nsmall-$1.00\nmedium-$1.50\nlarge-$2.00\n")).lower()
  while frenchfrysize not in frenchfrysizelist:
    frenchfrysize = input("Please select small, medium or large").lower()  
  if frenchfrysize == "small":
    megasize=(input("Would you like to megasize your fries? Yes/No: ")).lower()
    while megasize not in choice:
      megasize=(input("Please enter yes or no: ")).lower()
      if megasize =="no":
        total = total + 1
        print(f"You selected small\n\nYour current total is ${total:.2f}\n")
      total = total + 2
      print(f"You selected megasize\n\nYour current total is ${total:.2f}\n")
      
  elif frenchfrysize == "medium":
    total = total + 1.50
    print(f"You selected medium\n\nYour current total is ${total:.2f}\n")
  else:
    total = total + 2
    print(f"You selected large\n\nYour current total is ${total:.2f}\n")
#--------------------------------------------------------ketchup-------------------------------------------------------------
ketchupnum = input("How many keptchup packets would you like?\n")
while not ketchupnum.isnumeric():
  ketchupnum = input("Please enter a whole number greater than or equal to zero.\n")
if int(ketchupnum) >= 0:
  total = total + 0.25 * int(ketchupnum)

if selectedsandwhich != "" and beveragesize != "" and frenchfrysize != "":
  total = total - 1
  print("Because you selected a Sandwhich, French Fries and a Drink, you recieve a $1.00 discount\n")  
print(f"Your final total is ${total:.2f}")
  