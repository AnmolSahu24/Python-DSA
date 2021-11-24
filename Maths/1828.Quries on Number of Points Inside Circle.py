import math

class Solution:
    def countPoints(self, points, queries):
        ans = []

        for circle in queries:
            radius = circle[-1]
            count = 0

            for p in points:
                distance =self.CalcDistance(p[0], p[1], circle[0], circle[1])
                if distance <= radius:
                    count +=1
            ans.append(count)
        return ans



    def CalcDistance(self,pX,pY,cX,cY):
        #Euclidean Distance Formula
        root = pow(pX-cX, 2) + pow(pY-cY, 2)

        return math.sqrt(root)


points =  [[1,3],[3,3],[5,3],[2,2]]
queires = [[2,3,1],[4,3,1],[1,1,2]]
obj =Solution()
print(obj.countPoints(points,queires))