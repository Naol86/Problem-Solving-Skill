
from collections import defaultdict, deque


class DoubleLinkedList:
  def __init__(self, val=0, pre=None, next=None):
    self.val = val
    self.pre = pre
    self.next = next

def print_lis(node):
  while node:
    if node.val == 'a':
      break
    print(node.val, end=" ")
    node = node.next
  print()

def solve():
  
  tail = DoubleLinkedList('a')
  dummy = DoubleLinkedList(next=tail)
  tail.pre = dummy
  
  nodes = defaultdict(deque)
  
  for _ in range(int(input())):
    x = input().split()
    if len(x) == 3:
      __, val, after = x
      if int(after) in nodes:
        new_node = DoubleLinkedList(int(val), nodes[int(after)][0], nodes[int(after)][0].next)
        nodes[int(after)][0].next.pre = new_node
        nodes[int(after)][0].next = new_node
        nodes[int(val)].append(new_node)
      else:
        new_node = DoubleLinkedList(int(val), tail.pre, tail)
        tail.pre.next = new_node
        tail.pre = new_node
        nodes[int(val)].append(new_node)
    else:
      _, val = x
      if int(val) in nodes:
        node = nodes[int(val)].popleft()
        node.pre.next = node.next
        node.next.pre = node.pre
        if not nodes[int(val)]:
          del nodes[int(val)]
  print_lis(dummy.next)
solve()