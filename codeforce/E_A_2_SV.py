
class TreeNode:
  def __init__(self, val=0) -> None:
    self.val = val
    self.child = []

def print_lis(node):
  if not node:
    return 
  print(node.val, end="-->")
  for i in node.child:
    print_lis(i)
  print()

final = [0]
def find(node):
  if not node:
    return 0
  # print(node.child)
  if len(node.child) == 0:
    return 1
  ans = 0
  temp = []
  for child in node.child:
    x = find(child)
    ans += x
    temp.append(x)
  temp.sort()
  team = 0
  # print(temp)
  _sum = 0
  heap = []
  # for i in range(len(temp) - 1):
  #   _sum += temp[i]
    
  #   team += temp[i]
  #   temp[i+1] -= temp[i]
  for i in range(len(temp) - 1):
    while heap and temp[i]:
      x = -heap.pop()
      x -= 1
      
  final[0] += team
  ans -= (team * 2)
  # print(ans)
  return 1 + ans

for _ in range(int(input())):
  final = [0]
  n = int(input())
  boss = set([i + 1 for i in range(n)])
  nums = [int(i) for i in input().split()]
  nodes = {i:TreeNode(i) for i in range(1, n + 1)}
  for i in range(n - 1):
    if nums[i] != i + 1:
      nodes[nums[i]].child.append(nodes[i+1])
    if i + 1 in boss and i + 1 != nums[i]:
      boss.remove(i + 1)
  _set = set(nums)
  diff = boss.intersection(_set)
  # print_lis(nodes[1])
  root = TreeNode()
  root.child.append(TreeNode(n))
  dummy = TreeNode()
  dummy.child.append(root)
  for i in diff:
    root.child.append(nodes[i])
  find(dummy)
  print(final[0])
  # print(diff)