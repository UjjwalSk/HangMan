import random
import sys
import os

os.system("clear")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _   _                                         
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       

'''

words = ['Branch', 'Tusk', 'Ear', 'Frame', 'Lighthouse', 'Cord', 'Root', 'Stocking', 'Pencil', 'Camera', 'Drain', 'Watch', 'Popsicle', 'Fowl', 'Beehive', 'Sun', 'Snowball', 'Drop', 'Shirt', 'India', 'Blanket', 'Campfire', 'Knife', 'Coat', 'Hammer', 'Complete', 'Balloon', 'Eyebrow', 'Fireman', 'Bridge', 'Light Bulb', 'Hospital', 'Pool', 'Bicycle', 'Comb', 'Boat', 'Mosquito', 'Germany', 'Spongebob', 'Nose', 'Prison', 'Store', 'Cup', 'Picture', 'Bubblegum', 'Star', 'Toe', 'Wing', 'Bone', 'Line', 'Roof', 'Money', 'Gun', 'Birthday', 'Nightmare', 'Hook', 'Suitcase', 'Spring', 'Throat', 'Wheel', 'Map', 'Carriage', 'Lighthouse', 'Heart', 'Skeleton', 'Cushion', 'Chicken', 'Net', 'Owl', 'Horn', 'Country', 'Drawer', 'Head', 'Station', 'Flashlight', 'Sunshade', 'Bird', 'Ship', 'Commercial', 'Nerve', 'Treasure', 'Pineapple', 'Plough', 'Jellyfish', 'Music', 'Shoe', 'Gate', 'Stomach', 'Office', 'Bucket', 'Foot', 'Brain', 'Neck', 'Circle', 'Cat', 'House', 'Town', 'Tongue', 'Sponge', 'Monkey', 'Stomach', 'Worm', 'Tree', 'Cow', 'Book', 'Door', 'Cheese', 'Pot', 'Leg', 'Purse', 'Diamond', 'Bulb', 'Pipe', 'Face', 'Microphone', 'Sandbox', 'Blueberry', 'Sunglasses', 'Camera', 'Seahorse', 'Feather', 'Thread', 'Goat', 'Jalapeno', 'Eye', 'Jewel', 'Seed', 'Strawberry', 'Garden', 'Exercise', 'Sandwich', 'Dog', 'Nut', 'Scale', 'Moon', 'Thumb', 'Cart', 'Chimney', 'Pensioner', 'Skirt', 'Password', 'Blade', 'Face', 'Chain', 'Telephone', 'Bathroom', 'Toothbrush', 'Electricity', 'Engine', 'Match', 'Cake', 'Plane', 'Peach', 'Orange', 'Plate', 'Teapot', 'Wall', 'Rod', 'Ticket', 'Church', 'Tray', 'Girl', 'Spaceship', 'Photograph', 'Backpack', 'Toothpaste', 'Nail', 'Knee', 'Curtain', 'Landscape', 'Rat', 'Cowboy', 'Flute', 'Newspaper', 'Sail',
         'Shallow', 'Brake', 'Glove', 'Shelf', 'Sock', 'Stick', 'Needle', 'Window', 'Nature', 'Thief', 'Horse', 'Pen', 'Sheep', 'Button', 'Dress', 'Farm', 'Lip', 'Biscuit', 'Spade', 'Morning', 'Pump', 'Hand', 'Husband', 'Chess', 'Egg', 'Boot', 'Skate', 'Elephant', 'Basement', 'Potato', 'Rectangle', 'Leaf', 'Ring', 'Whistle', 'Flag', 'Skin', 'Muscle', 'Tail', 'Rug', 'Octopus', 'Mouth', 'Fly', 'Telescope', 'Snowball', 'Train', 'Brick', 'Horsewhip', 'Artist', 'Brush', 'Collar',
         'Pig', 'Trousers', 'Wire', 'Scissors', 'Outside', 'Boy', 'Lock', 'Finger', 'Wax', 'Receipt', 'Stamp', 'Pajamas', 'Printer', 'Swordfish', 'Board', 'Cloud', 'Key', 'Card', 'Internet', 'Hamburger', 'Knot', 'Fish', 'Rail', 'Snake', 'Pin', 'Spoon', 'Snowboard', 'Breakfast', 'Pocket', 'Sprinkler', 'Tooth', 'Whip', 'Dandelion', 'Fork', 'Bottle', 'Parcel', 'Florida', 'Cellphone', 'Cupcake', 'Popcorn', 'Knee', 'Stem', 'Umbrella', 'French', 'Table', 'Doormat', 'Building', 'Spinach', 'Street', 'America', 'Clock', 'Square', 'Doghouse', 'Hook', 'Box', 'Oven', 'Island', 'Kettle', 'School', 'Hat', 'Floor', 'Skyline', 'Screw', 'Chin', 'School', 'Hair', 'Deep', 'Hairbrush']


print(logo)
word = random.choice(words)
dashes = ["_ "]*len(word)
end = False
lives = 7

while not end:
    print(" ".join(dashes), '\n')
    letter = input("Guess a letter: ")
    if(not letter.isalpha()):
        print("Enter a valid letter")
        continue
    os.system("clear")
    letter = letter[0].lower()
    if(not letter.isalpha() or letter == ''):
        print("Enter a valid letter")
        continue
    if(letter in word.lower() and (letter not in dashes and letter.upper() not in dashes)):
        for i in range(len(word)):
            if(word[i].lower() == letter):
                dashes[i] = word[i]
    elif(letter in dashes or letter.upper() in dashes):
        print(f"You've already guessed {letter}")
    else:
        print(f"{letter} is not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end = True
            print("You lose.")
            print(f"The word was {word}.")
    if('_ ' not in dashes):
        end = True
        print("You win!!!")
        print(f"Word was {word}")

choice = input("Play again? [y/n]: ")
if(choice.lower() == 'y' or choice.lower() == 'yes'):
    os.system('python3 "'+sys.argv[0]+'"')
