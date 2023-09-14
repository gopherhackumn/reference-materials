import random
from string import ascii_lowercase
from substitute import substitute

def random_substitution():
    letters = list(ascii_lowercase) # list of all lowercase letters
    random_permutation = []
    while letters:
        letter = random.choice(letters)
        random_permutation.append(letter)
        letters.remove(letter)
    return {letter: other_letter for letter, other_letter in zip(ascii_lowercase, random_permutation)}

def main():
    # generate random substitution code
    sub = random_substitution()
  
    # get original text
    with open("bruh.txt") as f:
        text = f.read()

    # encrypt text using reordering
    encrypted_text = substitute(text, sub)
    with open("encrypted.txt", "w") as f:
        f.write(encrypted_text)
    
    print("done")

if __name__ == "__main__":
    main()