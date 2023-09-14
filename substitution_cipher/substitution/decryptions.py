from collections import Counter
from string import ascii_lowercase
from substitute import substitute
from kgram.fitness import KgramFrequency
from functools import cache

def substitution_by_frequency(message):
  letters_by_use = "etaoinshrdlcumwfgypbvkjxqz" # this is each letter in English ordered by usage off of Wikipedia
  message_frequency = Counter(message.lower()) # this associates each letter with the number of times it appears in the message
  letters_by_message_use = sorted(ascii_lowercase, key=lambda char: message_frequency[char], reverse=True) # order letters by usage in message
  unsub = {}
  for letter, original_letter in zip(letters_by_message_use, letters_by_use):
    unsub[letter] = original_letter
  return unsub

def naive_decrypt(message):
    unsub = substitution_by_frequency(message)
    return substitute(message, unsub)

@cache
def substitution_by_kgram_frequency(message, k=4):
  best_guess_unsub = substitution_by_frequency(message)
  kgram_freq = KgramFrequency(k)
  # now we swap substitutions greedily to maximize fitness of message
  swapped = True
  while swapped:
    swapped = False
    for letter in best_guess_unsub:
      print(best_guess_unsub)
      score = {}
      for candidate in best_guess_unsub:
        # swap candidate in
        best_guess_unsub[letter], best_guess_unsub[candidate] = best_guess_unsub[candidate], best_guess_unsub[letter]
        # record fitness
        score[candidate] = kgram_freq.fitness(substitute(message, best_guess_unsub))
        # swap candidate back out
        best_guess_unsub[letter], best_guess_unsub[candidate] = best_guess_unsub[candidate], best_guess_unsub[letter]
      # decide best candidate, assign, and remove from candidate pool
      best = max(score, key=score.get)
      if best != letter:
        swapped = True
        best_guess_unsub[letter], best_guess_unsub[best] = best_guess_unsub[best], best_guess_unsub[letter]
  return best_guess_unsub
  
def kgram_decrypt(message):
  best_guess_unsub = substitution_by_kgram_frequency(message, k=4)
  return substitute(message, best_guess_unsub)

def get_encrypted_text():
  with open("encrypted.txt") as f:
    encrypted_text = f.read()
  return encrypted_text

def write_to_file(filename, message):
  with open(filename, "w") as f:
    f.write(message)
    
def main():
  
  encrypted_text = get_encrypted_text()
  
  naive_decrypted_text = naive_decrypt(encrypted_text)

  write_to_file("naive_decrypted.txt", naive_decrypted_text)

  print("naive done")
  
  kgram_decrypted_text = kgram_decrypt(encrypted_text)

  write_to_file("kgram_decrypted.txt", kgram_decrypted_text)
    
  print("kgram done")

if __name__ == "__main__":
  main()