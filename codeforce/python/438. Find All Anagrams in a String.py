class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s+=" "
        count = []
        com = {}
        dic = {}
        if len(p) > len(s):
            return count 
        for i in range(len(p)):
            if p[i] in dic:
                dic[p[i]] +=1
            if p[i] not in dic:
                dic[p[i]] = 1
            if s[i] in com:
                com[s[i]] +=1
            if s[i] not in com:
                com[s[i]] = 1
        a = 0
        b = len(p)
        while b < len(s):
            if dic == com:
                count+=[a]
            if s[b] not in com and s[b] != " ":
                com[s[b]] = 1
            elif s[b] in com:
                com[s[b]] +=1
            com[s[a]] -=1
            if com[s[a]] == 0:
                com.pop(s[a])
            a+=1
            b+=1
        return count
