import java.util.*;
public class Dynamic{
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n=sc.nextInt();
            Integer dp[]=new Integer[n+1];
            int ans=Memo(n,dp);
            System.out.println(ans);
        }
    }
    public static int Memo(int n,Integer dp[]){
        //condition if value is present.
        if (n<=1){
            return n;
        }
        else{
            if (dp[n]!=null){
                return dp[n];
            }
        }
        int sp1=Memo(n-1,dp);
        int sp2=Memo(n-2,dp);
        //store
        dp[n]=sp1+sp2;
        return sp1+sp2;
    }
    public static int BUTabu(int n,Integer dp[]){
        dp[0]=0;
        dp[1]=1;
        for (int i=2;i<=n;i++){
            int sp1=dp[i-1];
            int sp2=dp[i-2];
            dp[i]=sp1+sp2;
        }
        return dp[n];
    }
}