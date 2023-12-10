public class recursion {
    private static int[] memo;

    public static void main(String[] args){
        int n=20;
        memo = new int[n];
        System.out.println("the recursive equation is g(n)=3g(n-1)-2g(n-2)");
        System.out.println("The first "+n+" terms of the recursive sequence are:");
        for(int i=0;i<n;i++)
            System.out.println((i+1)+". "+g(i));
    }

    public static int g(int n){
        if(n==0){
            return memo[0] = 1;
        }
        else if(n==1){
            return memo[1] = -1;
        }
        else{
            if(memo[n] != 0) return memo[n];
            return memo[n] = 3*g(n-1)-2*g(n-2);
        }
    }
}