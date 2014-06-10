class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 1: return x
        if n == 0: return 1

        v = pow(x, n / 2)

        return v * v * pow(x, n % 2)

if __name__ == '__main__':
    print pow(2, 6)
