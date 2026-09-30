while True:
    word = input ("Enter a Word:")
    letter = input ("Enter a character to search for:")

    found = False

    for character in word:
        if character.lower() == letter.lower():
            found = True

            break

    if found:
        print("Character found!")
    else:
        print("Character not found.")

    again = input("Try again? (Y/N):")

    if again.upper() != "Y":
        break