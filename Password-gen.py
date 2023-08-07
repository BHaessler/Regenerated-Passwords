#calling modules
"""Random module for picking letters for the passwords"""
import random

"""Import messagebox from tkinter module """
import tkinter.messagebox

#---------------------------------------------------------------------------------
# this is a password generator that will ask the user how many passwords they
# want generated, how difficult they want the passwords to be and how long
# they want them to be
#---------------------------------------------------------------------------------

def get_user_input():
    """Gathers user inputs for the password creations"""

    user_number = input("How many passwords would you like to create today?\n")
    print("Thanks")
    user_len = input("How long would you like your passwords to be?\n")
    print("Thanks again. Final Question")
    user_diffi = input("How difficult would you like your passwords to be (E ="
    + " just letters, uppercase and lowercase, M = letters and numbers, H = letters, "
    + "numbers and symbols) [enter corresponding letter]?\n").lower()
    return user_number, user_diffi, user_len



def create_char_list(difficulty):
    """Creates a list of viable characters/letters for the passwords to be made from"""

    e_list = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H",
            "i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q"
            ,"Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
    m_list_adds = ["1","2","3","4","5","6","7","8","9","0"]
    h_list_adds = ["~","`","!","@","#","$","%","^","&","*","?","/"]
    final_char_list = []

    if difficulty == "e":
        final_char_list = final_char_list + e_list
        return final_char_list

    elif difficulty == "m":
        final_char_list = e_list + m_list_adds
        return final_char_list

    elif difficulty == "h":
        final_char_list = e_list + m_list_adds + h_list_adds
        return final_char_list



def create_passwd(char_list, number_of_pws, pwd_len):
    """Given the characters to pick from, the number of passwords to make, and
     the length, this will create the passwords the user has asked for
    """

    password_list = []

    for password in range(0, number_of_pws):
        password_string = ""
        for additive in range(0, pwd_len):
            password_string = password_string + random.choice(char_list)
        password_list.append(password_string)

    return password_list



def final_printout(password_list):
    """a function that prints the final password list
    """
    print("\nThese are your randomly generated passwords:")
    for password in password_list:
        print(password)
    print("\n")
    return None



def print_out(password_list):
    """This is a function that will give the user the option to output the
    passwords into a file. It requires that the password list be passed as 
    an arguement
    """
    file_name = input("What do you want to name your file of passwords? \n")

    with open(file_name + ".txt", "a") as file1:
        for item in password_list:
            file1.write(item + "\n")

    print("\nYour file has been created")   
    return



def on_click(passwords_to_print):
    """A function to put the passwords into a pop out window for the user. This 
    function required the list of passwords as an argument to be passed."""
    str_print = ""
    for item in passwords_to_print:
        str_print += item
        str_print += "\n"
    tkinter.messagebox.showinfo("Your Passwords", str_print)
    return



"""Main code is here, calls functions in order of usage"""

#defining global variables
user_number = 0
user_len = 0
user_diffi = "0"

#taking in user input
user_number, user_diffi, user_len = get_user_input()
user_number = int(user_number)
user_len = int(user_len)
    
char_list = create_char_list(user_diffi)
#print(char_list)
password_final = create_passwd(char_list, user_number, user_len)
    
question = input("Do you want to see the passwords? [yes or no] \n").lower()
if question == "yes"
    final_printout(password_final)

file_create = input("Do you want to create a file with these passwords? [yes or no] \n").lower()
if file_create == "yes":
    print_out(password_final)

file_pop = input("Do you want to have popout window create with these passwords?"
+ " [yes or no] \n").lower()
if file_pop == "yes":
    on_click(password_final)

print("\nThank you for using the password generator today!")



main_func() #calls "main" for ease of reading
