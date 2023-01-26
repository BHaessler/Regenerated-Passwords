# this is a password generator that will ask the user how many passwords they 
# want generated, how difficult they want the passwords to be and how long 
# they want them to be

#calling modules 
import random

#defining global variables
userNumber = 0
userLen = 0
userDiffi = "0"


#asks the user for their input 
def get_user_input():
    userNumber = input("How many passwords would you like to create today?\n")
    print("Thanks")
    userLen = input("How long would you like your passwords to be?\n")
    print("Thanks again. Final Question")
    userDiffi = input("""How difficult would you like your passwords to be (e =
     just letters, uppercase and lowercase, m = letters and numbers, h = letters, 
     numbers and symbols) [enter corresponding letter]?\n""").lower()
    return userNumber, userDiffi, userLen


#a function that creates the charactor list to randomly pick from 
def create_char_list(difficulty):
    e_list = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H",
            "i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q"
            ,"Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
    m_list_adds = ["1","2","3","4","5","6","7","8","9","0"]
    h_list_adds = ["~","`","!","@","#","$","%","^","&","*","?","/"]
    final_char_list = []

    if difficulty == "e":
        final_char_list = final_char_list + e_list 
        return (final_char_list)

    elif difficulty == "m": 
        final_char_list = e_list + m_list_adds
        return(final_char_list)

    elif difficulty == "h":
        final_char_list = e_list + m_list_adds + h_list_adds
        return(final_char_list)

#a function that creates as many passwords as the user has asked for 
def create_passwd(char_list, number_of_pws, pwd_len):
    password_list = []

    for password in range(0, number_of_pws):
        password_string = ""
        for additive in range(0, pwd_len):
            password_string = password_string + random.choice(char_list)
        password_list.append(password_string)

    return(password_list)

#a function that prints the final password list
def final_printout(password_list):
    print("\nThese are your randomly generated passwords:")
    for password in password_list:
        print(password)
    print("\n")
    return None

#main code is here 
#calls functions in order of usage
userNumber, userDiffi, userLen = get_user_input()
userNumber = int(userNumber)
userLen = int(userLen)
# print(userNumber)
# print(userDiffi)
# print(userLen)
char_list = create_char_list(userDiffi)
#print(char_list)
password_final = create_passwd(char_list, userNumber, userLen)
final_printout(password_final)
