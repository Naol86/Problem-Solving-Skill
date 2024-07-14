n, k = map(int, input().split())
s = input()
letters = [0] * k
for i in s:
  if ord(i) - ord("A") < k:
    letters[ord(i) - ord("A")] += 1
letters.sort()
print(letters[0] * k)