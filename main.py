print("This is clasic hangman")
word = input("Enter a word (Please do not use upercase letters.)")
counter =0
letters = len(word)

print("there are " + str(letters) + " letters in the word")
tries = 6
alreadyGuessed = []
Lists = []
index = 0

for n in range(letters):
    Lists.append(word[index])
    index = index + 1
print(Lists)


while (Lists != []):
    Guess = input("Enter a letter ")
    if (Guess in alreadyGuessed):
      print("Looks like you already guess that letter")
      for i in range(len(Lists)):
        if Guess == Lists[counter]:
          Lists.remove(Guess)
          counter+=1
      counter = 0
    for n in range(letters):
      if (Guess == Lists[counter]):
          number=counter+1
          print("You gessed a correct letter, you guessed letter number " + str(number))
      counter=counter+1
    if (Guess not in Lists):
        print("You gessed the wrond letter")
        tries = tries - 1
    if (tries < 0):
        print("GAME OVER!  looks like you took to many tries.")
        break
    
    alreadyGuessed.append(Guess)
    counter = 0
if Lists == []:
  print("Looks like you won")