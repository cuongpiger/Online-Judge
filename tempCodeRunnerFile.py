from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cache = {}
        n = len(grid)
        for i in range(n):
            hv = hash(tuple(grid[i]))
            v = cache.get(hv, None)
            if v is None:
                cache[hv] = [1, 0]
            else:
                cache[hv] = [v[0] + 1, v[1]]

            hv = hash(tuple([grid[j][i] for j in range(n)]))
            v = cache.get(hv, None)
            if v is None:
                cache[hv] = [0, 1]
            else:
                cache[hv] = [v[0], v[1] + 1]

        cnt = 0
        for k, v in cache.items():
            cnt += v[0] * v[1]

        return cnt
    
sol = Solution()

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(sol.equalPairs(grid))