import java.util.Scanner;
import java.util.Arrays;
public class CountEvenOdd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("n: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[] count = new int[5];
        for (int x : arr) {
            if (x % 2 == 0) count[0]++; else count[1]++;
            if (x > 0) count[2]++;
            else if (x < 0) count[3]++;
            else count[4]++;}
        System.out.println("Even: " + count[0]);
        System.out.println("Odd: " + count[1]);
        System.out.println("Positive: " + count[2]);
        System.out.println("Negative: " + count[3]);
        System.out.println("Zero: " + count[4]);
        System.out.println("Array: " + Arrays.toString(arr));
    }
}
