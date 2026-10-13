class Solution {
    public int maximumWealth(int[][] accounts) {
        int a=0,i,j;
        for(i=0;i<accounts.length;i++){
            int s=0;
            for(j=0;j<accounts[i].length;j++){
                 s += accounts[i][j];

            }
            if (s > a) {            
                a = s;
        }
       
    } return a;
    }}