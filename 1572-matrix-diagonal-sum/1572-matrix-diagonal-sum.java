class Solution {
    public int diagonalSum(int[][] mat) {
        int n= mat.length;
        int m =Math.floorDiv(n,2);
        int s=0;
        for(int i=0;i<n;i++){
            s+=mat[i][i];
            s+=mat[n-i-1][i];
        }if(n%2==1){
            s-=mat[m][m];
        }
          return s;  }
}