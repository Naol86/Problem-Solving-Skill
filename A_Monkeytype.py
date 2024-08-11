for _ in range(int(input())):
  keys = input()
  word = input()
  
  places = {}
  for i in range(26):
    places[keys[i]] = i
  
  time = 0
  
  for i in range(1, len(word)):
    time += abs(places[word[i-1]] - places[word[i]])
  
  print(time)