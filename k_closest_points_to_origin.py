## Question
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Example
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

## Constraints
# 1 <= k <= points.length <= 104
# -104 < xi, yi < 104

## My Solution - Using Heap Data Structure
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Euclidean Distance
        dist = []
        for point in points:
            dist_ = (point[0]**2 + point[1]**2)
            dist.append([dist_, point[0], point[1]])

        heapq.heapify(dist)
        ans = []
        
        while k > 0:
            euc_dist, x, y = heapq.heappop(dist)
            ans.append([x, y])
            k -= 1

        return ans


    
