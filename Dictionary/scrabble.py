letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# list comprehension and zip, that has the elements of letters (keys) and points (values)
letter_to_points = {key:value for key, value in zip(letters, points)}

# add a key of " " and value of 0 to letter_to_points 
letter_to_points[" "] = 0 

# function score_word(word) 
def score_word(word):
    point_total = 0 # local variable 
    # loop that goes through word and adds the value to point_total, 0 if doesn't exist 
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points) # runs // output = 15 

player_to_words = { 
    "player1" : ["BLUE", "TENNIS", "EXIT"], 
    "wordNerd" : ["EARTH", "EYES", "MACHINE"], 
    "LexiCon" : ["ERASER", "BELLY", "HUSKY"], 
    "ProfReader" : ["ZAP", "COMA", "PERIOD"]
    }

player_to_points = {} 

# iterate through player_to_words, key:word = player:words
for player, words in player_to_words.items():
    player_points = 0 
    # 1. loop that goes through each word in words 
    for word in words:
        # 2. get a value of the word and add it to player_points 
        player_points += score_word(word)
    # update dict player_to_points like {player:score}
    player_to_points.update({player : player_points})

# wordNerd should be winning by 1 point 

print(player_to_points) # runs 

# play_word // a function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, word):
    word = word.upper()
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        print("This player doesn't exist!")

play_word("player1", "success")
print(player_to_words)
