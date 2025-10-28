import string
name = input("Hi 👋 there. What's your name?")
print(f"Hello {name} and welcome to our word and character count program")

while True:
    sentence = input("Enter a sentence (or type 'quit' to stop): ")
    if sentence.lower() == 'quit':
        print(f'''This program has officially ended!
        Thank you {name} for your amiable participation''')
        break
    while True:
     User_choice = input("Do you want to count 'words' or 'characters' or 'both' ?").strip().lower()
     if User_choice in ["words", "characters", "both"]:
      break
     else:
      print("Please enter only the valid options")
    while True:
     ignore_space = input("Ignore spaces? (yes/no): ").strip().lower() 
     if ignore_space in ["yes", "no"]:
      break
     else:
      print("Please enter yes or no only")
    while True:
     ignore_punctuation = input("Ignore punctuation? (yes/no): ").strip().lower()
     if ignore_punctuation in ["yes", "no"]:
      break
     else:
      print("Please enter yes or no only")
    
    # Count words
    words = sentence.split()
    word_count = len(words)
    
    # Process for character counting
    processed_sentence = sentence
    if ignore_punctuation == "yes":
        processed_sentence = ''.join(char for char in processed_sentence if char not in string.punctuation)
    if ignore_space == "yes":
        processed_sentence = processed_sentence.replace(" ", "")
    
    char_count = len(processed_sentence)
    if User_choice == "words":
     print(f"Word count: {word_count}")
    if User_choice == "characters":
     print(f"Character count: {char_count}")
    if User_choice == "both":
     print(f"Word count: {word_count}")
     print(f"Character count: {char_count}")
     

