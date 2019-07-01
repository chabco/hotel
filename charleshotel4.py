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

### Display a menu asking whether to check in or check out.
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
			checkOut()
			return False
			stayingNow = False
		elif askGuest.lower() == 'check in':
			print('Welcome! Let\'s get your information to check in!')
			checkIn()
			return True
			stayingNow = False
		else:
			print('Sorry, I didn\'t get that.')
			continue

def checkOut():
    askFloor = input('Which floor are you staying on?')
    if int(askFloor) != ['1', '2', '3']:
        askRoom = input('...And which room?')
        if hotel.get(askFloor) and hotel.get(askFloor).get(askRoom) != None:
            del hotel[askFloor][askRoom]
            print(hotel)
            print('Goodbye.')
        else:
            print('You are not in our books...*awkward pause*')
    else:
        print('We only have three floors...')

def checkIn():
	guestAmount = 0
	guestList = []
	howMany = input('How many guests will be staying with us?: ')
	while int(howMany) > 1:
		name = input('Please provide the names of guests: ')
		guestList.append(name)
		guestAmount += 1
	print(guestList)
