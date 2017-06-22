from spy_details import spy, Spy, ChatMessage, friends        # import spy from spy_details
from termcolor import colored                                 # import colored from termcolor
from steganography.steganography import Steganography         # import steganography from steganography
from datetime import datetime                                 # import datetime from datetime
# define the status message
STATUS_MESSAGES = ['Hey! Im using spyChat !','hardworking is the best way to do always in life',]


print colored("Hello! Welcome to the spy chat application","red")

question = colored("Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? ","green")
existing = raw_input(question)

#define the status add to it
def add_status():
# condition show updated status message is none because status message is not updated
    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % spy.current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
# condition show that status message is not update then new status message is set
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message =new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:

            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % updated_status_message
    else:
        print 'You current don\'t have a status update'

    return updated_status_message



# define the friend to be added
def add_friend():
    new_friend = Spy('','',0,0.0)
#new friend is added
    new_friend.name = raw_input(" add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")



    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print colored( 'Friend Added',"red")

    else:
        print colored( 'Wrong! Invalid entry. It can\'t add spy with the details you provided',"blue")

    return len(friends)


#   select friend that is added
def select_a_friend():
    item_number=0
    for friend in friends:
        print colored('%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                friend.age,
                                                                friend.rating),'blue')
        item_number = item_number + 1
#condition choose the friend from selected friend
    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

# send messsage after selecting the friend
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "steganography.jpg"
    text = raw_input("What do you want to say? ")
    #condition it encode the origina image,text,output path and message shown in image is secret
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print colored("Your secret message image is ready!","blue")

# read the message after being send to the choosen friend
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)
    print secret_text

    if len(secret_text) > 100: # condition shows that secret of the message text greater than 100
        friends.pop(sender)    # then list of the message of the send delete
    elif secret_text == "SOS": # condition shows that if the secret text show message SOS
        print colored( "may god bless every one","red") # then show the appropriate message
    elif secret_text == "SAVE ME":
        print colored("you should be protected by us","blue")
    elif secret_text == "HELP ME":
        print colored("we should help you","red")
    else:
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chats.append(new_chat)
        print colored("Your secret message has been saved!","red")

# read chat history after being read the message send to the friend
def read_chat_history():

    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        #condition shows that if the message sent by my side shows the message in which day ,time and what message i have sent
        if chat.sent_by_me:
            print colored ('[%s] %s: %s' % (colored(chat.time.strftime("%d %B %Y %H:%M"),"red"), colored('Me','blue'), chat.message))
        else:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y %H: %M"), friends[read_for].name, chat.message)

# after read the chat history start the chat with the other friend
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age >  12 and spy.age <  50:


        print colored("\nAuthentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Welcome on spychat\n ","red")

        show_menu = True
        #show the choices you want to do with the friend

        while show_menu:
                menu_choices =  "What do you want to do? \n  1. Add a status update \n  2. Add a friend \n  3. Send a secret message \n  4. Read a secret message \n  5. Read Chats from user \n  6. Close Application \n"
                menu_choice = raw_input(menu_choices)
                menu_choice = int(menu_choice)





                if menu_choice == 1: # condition shows if the choice is 1 then add current status
                    spy.current_status_message = add_status()
                elif menu_choice == 2:  #condition shows if the choice is 2 then add friend
                    number_of_friends = add_friend()
                    print 'You have %d friends' % number_of_friends

                elif menu_choice == 3: # condition shows if the choice is 3 then send secret message
                    send_message()
                elif  menu_choice == 4: # condition shows if the choice is 4 then read the message
                    read_message()
                elif  menu_choice == 5: # condition shows if the choice is 5 read chat history of the message
                    read_chat_history()
                else:
                    show_menu = False # condition shows if the choice is 6  close the application


    else:

        print colored('Sorry you are not capable of the correct age to be a spy',"red")

if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, tell me your spy name first")

    if len(spy.name) > 0:
        spy.salutation =  raw_input("Can I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'