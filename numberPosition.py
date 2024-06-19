from collections import Counter
import random


def getNumber():
  count = {}

  while len(count) != 4:
    number = random.randint(1234,9876)
    number = str(number)
    count = Counter(number)
    if '0' in count:
      count.pop('0')
  return (number)


def checker(guess, actual):
  p = n = 0
  for i in range(len(guess)):
    if guess[i] in actual:
      n += 1
      if guess[i] == actual[i]:
        p += 1
  return (n, p)


def main():
  number = getNumber()
  # print(number)

  guess = '0'

  while guess != number:
    guess = input()
    n, p = checker(guess, number)
    print(n, p)
  print("u got it")


if __name__ == "__main__":
  main()