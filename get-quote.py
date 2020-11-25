import random

def primary():
  f = open("quotes.txt", "a")
  f.writelines("See you soon!\n")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[random.randint(0,len(quotes)-1)][:-1]
    +"\n"+
    quotes[random.randint(0,len(quotes)-1)][:-1])

  print(f"file len: {len(quotes)}")

if __name__== "__main__":
  primary()
