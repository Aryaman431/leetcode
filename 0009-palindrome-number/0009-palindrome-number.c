bool isPalindrome(int x) {
 if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }
  long long a=x;
  long long b=0;
  while(a!=0){
    b= (a%10)+(b*10);
    a=a/10;
  }  
 return b==x;
}