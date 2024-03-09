class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lis = []
        a = 0
        while a < len(asteroids):
            if len(lis) == 0:
                lis.append(asteroids[a])
                a+=1
            elif lis[-1] * asteroids[a] > 0:
                lis.append(asteroids[a])
                a+=1
            elif lis[-1] < 0 and asteroids[a] > 0:
                lis.append(asteroids[a])
                a+=1
            else:
                if abs(asteroids[a]) == lis[-1]:
                    lis.pop()
                    a+=1
                elif abs(asteroids[a]) > lis[-1]:
                    lis.pop()
                else:
                    a+=1
        return lis
