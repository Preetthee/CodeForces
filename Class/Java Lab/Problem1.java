import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        boolean[] done = new boolean[n];
        int maxCount = 0;
        int maxVal = 0;

        for (int i = 0; i < n; i++) {
            if (done[i]) {
                continue;
            }

            int count = 0;

            for (int j = i; j < n; j++) {
                if (a[j] == a[i]) {
                    count++;
                    done[j] = true;
                }
            }

            System.out.println(a[i] + " -> " + count);

            if (count > maxCount) {
                maxCount = count;
                maxVal = a[i];
            }
        }

        System.out.println("Highest frequency: " + maxVal);
    }
}