#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Two things are missing from the line below - fill them in
my_user=UserAccount("mahmood","meetyear18","i am 15 years old")

#Call the print_secret method (function) - it takes one input - a guess for the password.
#Use the wrong password as input here
my_user.print_secret("meet")

#Use the right password here
my_user.print_secret("meetyear18")

