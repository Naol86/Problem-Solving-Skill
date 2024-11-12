# class SegmentTree:
#   def __init__(self, arr) -> None:
#     self.n = len(arr)
#     self.arr = arr
#     self.tree = [0] * (4 * self.n)
#     self.build(0, 0, self.n - 1)

#   def getChildren(self, node):
#     l = node * 2 + 1
#     r = node * 2 + 2
#     return l, r
  
#   def build(self, node, nLeft, nRight):
#     if nLeft == nRight:
#       self.tree[node] = self.arr[nLeft]
#       return
#     nMid = nLeft + (nRight - nLeft) // 2
#     l_child, r_child = self.getChildren(node)
    
#     self.build(l_child, nLeft, nMid)
#     self.build(r_child, nMid + 1, nRight)
    
#     self.tree[node] = self.tree[l_child] + self.tree[r_child]
  
#   def update(self, node, nLeft, nRight, index, value):
#     if nLeft == nRight:
#       self.arr[index] = value
#       self.tree[node] = value
#       return
    
#     nMid = nLeft + (nRight - nLeft) // 2
#     l_child, r_child = self.getChildren(node)
    
#     if index <= nMid:
#       self.update(l_child, nLeft, nMid, index, value)
#     else:
#       self.update(r_child, nMid + 1, nRight, index, value)
    
#     self.tree[node] = self.tree[l_child] + self.tree[r_child]
  
#   def query(self, node, nLeft, nRight, qLeft, qRight):
#     if  qLeft > qRight:
#       return 0
#     if qLeft == nLeft and qRight == nRight:
#       return self.tree[node]

#     nMid = nLeft + (nRight - nLeft)//2
#     l_child, r_child = self.getChildren(node)
    
#     left_sum = self.query(l_child, nLeft, nMid, qLeft, min(qRight, nMid))
#     right_sum = self.query(r_child, nMid + 1, nRight, max(nMid + 1, qLeft), qRight)
    
#     return left_sum + right_sum

class SegmentTree:
  def __init__(self, arr) -> None:
    self.n = len(arr)
    self.arr = arr
    self.tree = [0] * (2*self.n)
    self.build()
  
  def build(self):
    for index in range(self.n):
      self.tree[index + self.n] = self.arr[index]
    
    for index in range(self.n - 1, 0, -1):
      self.tree[index] = self.tree[index << 1] + self.tree[index << 1 | 1]
  
  def update(self, index, value):
    self.arr[index] = value
    index += self.n
    self.tree[index] = value
    
    while index > 1:
      self.tree[index >> 1] = self.tree[index] + self.tree[index ^ 1]
      index >>= 1
  
  def query(self, left, right):
    left += self.n
    right += self.n
    range_sum = 0
    while left < right:
      if left & 1:
        range_sum += self.tree[left]
        left += 1
      if right & 1:
        right -= 1
        range_sum += self.tree[right]
      left >>= 1
      right >>= 1
    return range_sum