hotel = {
 '1': {
   '101': ['George Jefferson', 'Wheezy Jefferson'],
 },
 '2': {
   '237': ['Jack Torrance', 'Wendy Torrance'],
 },
 '3': {
   '333': ['Neo', 'Trinity', 'Morpheus']
 }
}

# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.


def visitorStatus():
    stayingNow = True
    while stayingNow:
        askGuest = input('Hello, will you check in or check out?: ')
        if askGuest.lower() == 'check out':
            print('Thank you for staying with us. Please provide your information to check out.')
            return False
            stayingNow = False
        elif askGuest.lower() == 'check in':
            print('Welcome! Let\'s get your information to check in!')
            return True
            stayingNow = False
        else:
            print('Sorry, I didn\'t get that.')
            continue


visitorStatus()