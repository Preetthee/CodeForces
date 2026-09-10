import java.util.Scanner;

public class SearchFrequency {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("N: ");
        int n = sc.nextInt();
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) arr[i] = sc.next();
        System.out.print("x: ");
        String x = sc.next();

        int count = 0;
        StringBuilder pos = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (arr[i].equals(x)) {
                pos.append(i).append(" ");
                count++;
            }
        }

        System.out.println(count > 0 ? "Found" : "Not found");
        if (count > 0) System.out.println("Positions: " + pos);
        System.out.println("Frequency: " + count);
    }
}
