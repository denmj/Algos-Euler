class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
                
        max_ = arr.index(max(arr))
        
        if len(arr) < 3 or len(arr[1:max_+1]) == 0 or len(arr[max_+1:]) == 0:
            return False
        
        
        inc = arr[0]
        dec = max(arr)
        
        for i in arr[1:max_+1]:
            if inc >= i:
                return False
                break
            inc = i

        for j in arr[max_+1:]:
            print(dec, j)
            if j >= dec:
                return False
                break
            dec = j
        return True
