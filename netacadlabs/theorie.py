print("Hello World!")
str1="cisco"
str2="networking"
str3="academy"
print(str1+str2+str3)
# no space
print(str1,str2,str3)
# space
#print("The value of x is " + x) error bc wrong type
x=3
print("The value of x is " + str(x))
type(x)
x=str(x)
type(x)
num = 22/7
f"The value of num is {num}"
# . With f-strings, you can directly embed variables and expressions inside strings using curly braces {}.
pi = "{:.2f}".format(num)
f"The value of pi is {pi}."

# a list variable is used to store multiple pieces of ordered information = array
#create a list with [], separate the items with a commma
# type() to verify the datatype
# len() to return the number of items in a list
hostnames=["R1","R2","R3","S1","S2"]
type(hostnames)
len(hostnames)
hostnames
#An item in a list can be referenced and manipulated using its index.
# The first item in a list is indexed as zero, the second is indexed as one, and so on.
# The last item can be referenced with index [-1].
# Replace an item by assigning a new value to the index
#Use the del command to remove an item from a list.
hostnames[0]
hostnames[-1]
hostnames[0]="RTR1"
del hostnames[3]

#Dictionaries are unordered lists of object
#  Each object contains a key/value pair
#Create a dictionary using the braces { }.
# Each dictionary entry includes a key and a value.
# Separate a key and its value with a colon.
# Use quotes for keys and values that are strings.
ipAddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
type(ipAddress)
#use keys to reference to objects in dicts
# the key is enclosed in []
#single or double quotes
# use a key in the dictionary statement to verify if a key exists in the dictionary.
# Add a key/value pair by setting the new key equal to a value.

ipAddress['R1']
ipAddress["S1"]="10.1.1.10"


# use the input() function which includes an optional parameter to provide a prompt string. 
firstName = input("What is your first name? ")
print("Hello " + firstName +"!")
