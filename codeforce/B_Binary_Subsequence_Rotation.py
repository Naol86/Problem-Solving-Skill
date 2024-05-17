x = int(input())
s = input()
t = input()
s1 = s.count("1")
t1 = t.count("1")
if s1 != t1:
  print(-1)
elif s1 == t1 and (s1 == 0 or s1 == x):
  print(0)
else:
  def cal(s, t):
    s_lis = []
    t_lis = []
    nums = []

    for i in range(x):
      if s[i] != t[i]:
        s_lis.append(s[i])
        t_lis.append(t[i])
        if s[i] == '1':
          nums.append(1)
        else:
          nums.append(-1)
    nums2 = []
    temp = 0
    pre = 0
    for i in range(len(nums)):
      if pre != nums[i]:
        nums2.append(temp)
        pre = nums[i]
        temp = 0
      else:
        temp += 1
    return 0
  a = cal(s, t)
  print(a)