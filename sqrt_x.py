class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0: return 0
        if x < 4: return 1

        l = 2
        r = x / 2

        while l <= r:
            mid = l + (r - l) / 2
            if mid > x / mid:
                r = mid - 1
            elif mid < x / mid:
                l = mid + 1
                last_mid = mid
            else:
                return mid

        return last_mid

if __name__ == '__main__':
    import math
    print Solution().sqrt(6)
