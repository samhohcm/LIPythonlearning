# 
# Example file for retrieving data from the internet
#

import urllib.request # classes and code for html requests

def main():
    webURL = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webURL.getcode()))
    data = webURL.read()
    print(data)

if __name__ == "__main__":
  main()
