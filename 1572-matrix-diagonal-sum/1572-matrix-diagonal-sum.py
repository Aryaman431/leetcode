class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n=len(mat)
        m=n//2
        s=0
        for i in range(n):
            s+=mat[i][i]
            s+=mat[n-1-i][i]
        if n%2==1:
            s-=mat[m][m]
        return s
        