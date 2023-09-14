# check out http://practicalcryptography.com/media/cryptanalysis/files/ngram_score_1.py
from math import log
from string import ascii_letters
from collections import defaultdict
HOME = "/home/runner/GopherHackMar22"


class KgramFrequency:
  def __init__(self, k=4):  
    kgram_files = {
      1: f"{HOME}/substitution/kgram/english_monograms.txt",
      2: f"{HOME}/substitution/kgram/english_bigrams.txt",
      3: f"{HOME}/substitution/kgram/english_trigrams.txt",
      4: f"{HOME}/substitution/kgram/english_quadgrams.txt",
      5: f"{HOME}/substitution/kgram/english_quintgrams.txt"
    }
    self.k = k
    self.frequency = defaultdict(int)
    total = 0
    with open(kgram_files[self.k]) as f:
      for line in f:
        kgram, count_str = line.rstrip().split()
        count = int(count_str)
        self.frequency[kgram] = count
        total += count
    for kgram in self.frequency:
      self.frequency[kgram] /= total

  def fitness(self, message):
    # p(message) = product of p(kgram) for each contiguous kgram in message
    # for example with k = 4, p("attack") = p("atta") * p("ttac") * p("tack")
    # computer has limited precision when multiplying many values in [0, 1] range
    # so we can compute a sum instead of a product with logarithms
    # log(p("attack")) = log(p("atta")) + log(p("ttac")) + log(p("tack"))
    message = "".join(char.upper() for char in message if char in ascii_letters)
    score = 0
    for i in range(len(message) - self.k):
      kgram = message[i: i + self.k]
      probability = self.frequency[kgram]
      if probability == 0:
        score -= 30 # just choose (high) penalty instead of -infinity
      else:
        score += log(probability)
    return score

if __name__ == "__main__":
  m = KgramFrequency()
  print(m.frequency["TION"])
  candidates = ["FYYFHP YMJ JFXY BFQQ TK YMJ HFXYQJ FY IFBS", "i love my mom, i love my grandma", "sdjfhsdkfjhasgjfhbvoqpifhnasfadf", "fhakjsvhasiqojebgnzowuthvnjsr", "ATTACK THE EAST WALL OF THE CASTLE AT DAWN"]
  candidates.sort(key=m.fitness)
  print(candidates)

    