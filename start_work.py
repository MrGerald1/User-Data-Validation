import random
import string

big_dict={}
first_name=input('Please enter your first name: ').capitalize()
last_name=input('Please enter your last name: ').capitalize()
email=input('Please enter your email: ')

big_dict['first name']=[first_name]
big_dict['last name']=[last_name]
big_dict['Email']=[email]

alphabets=string.ascii_letters
word="".join(random.sample(alphabets,k=5))
# this returns the word with 5 randoms letters from alphabets without repitition

joined= ''.join([first_name[0:2],last_name[-2:],word])
password=''.join(random.sample(joined,k=9))
print('Your password is: ', password)

# print('Do you like this password? ', password)
answer=input('Do you like this password? ').lower()
while answer != 'yes' and answer != 'no':
    answer=input('Please enter yes or no: ').lower()
if answer=='no':
    new_pass=input('Enter a password greater than 7 characters: ')
    while len(new_pass)<7:
        print('Your password is less than 7 characters')
        new_pass=input('Please enter a password greater than 7 characters: ')
    # print(new_pass)
    big_dict['Password']=[new_pass]
elif answer=='yes':
    # print(password)
    big_dict['Password']=[password]
print('Your details are:', big_dict)
def user():
    a= input('Please enter your first name: ')
    b= input('Please enter your last name: ')
    c= input('Please enter your email: ')
    
    big_dict['first name'].append(a.capitalize())
    big_dict['last name'].append(b.capitalize())
    big_dict['Email'].append(c.capitalize())
    
    spt= a[0:2]
    dpt= b[-2:]
    
    alphabets=string.ascii_letters
    word="".join(random.sample(alphabets,k=5))
    # this returns the word with 5 randoms letters from alphabets without repitition

    joined= ''.join([spt,dpt,word])
    password=''.join(random.sample(joined,k=9))
    print('Your password is: ', password)

    # print('Do you like this password? ', password)
    answer=input('Do you like this password? ').lower()
    while answer != 'yes' and answer != 'no':
        answer=input('Please enter yes or no: ').lower()
    if answer=='no':
        new_pass=input('Enter a password greater than 7 characters: ')
        while len(new_pass)<7:
            print('Your password is less than 7 characters')
            new_pass=input('Please enter a password greater than 7 characters: ')
        print('This is your password',new_pass)
        big_dict['Password'].append(new_pass)
    elif answer=='yes':
        # print(password)
        big_dict['Password'].append(password)

    print(big_dict)

# New user? Continue

ans= input("Would you like to add a new employee? ")
while ans != 'yes' and ans != 'no':
    ans=input('Please enter yes or no: ').lower()
while ans=='yes':
    user()
    ans= input("Would you like to add a new user? ")
print('Current employees: ', big_dict)    