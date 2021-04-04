from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hmap = {arr[a]:a for a in range(len(arr))}
        print(hmap)
        print(hmap[0])
        for i in range(len(pieces)):
            if len(pieces[i])>1:
                for k in range(len(pieces[i])-1):
                    if pieces[i][k] not in hmap or pieces[i][k+1] not in hmap:
                        return False
                    if hmap[pieces[i][k+1]]-hmap[pieces[i][k]]>1 or hmap[pieces[i][k]]>hmap[pieces[i][k+1]]:
                        return False
            else:
                if pieces[i][0] not in hmap:
                    return False
        return True

arr = [85]
pieces = [[85]]
cl = Solution()
print(cl.canFormArray(arr, pieces))

arr = [49,18,16]
pieces = [[16,18,49]]
cl = Solution()
print(cl.canFormArray(arr, pieces))

arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]
cl = Solution()
print(cl.canFormArray(arr, pieces))