import java.util.*;

public class MaximumSubarray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        int current = arr[0];
        int maxSum = arr[0];

        for (int i = 1; i < n; i++) {
            current = Math.max(arr[i], current + arr[i]);
            maxSum = Math.max(maxSum, current);
        }

        System.out.println("Maximum Subarray Sum: " + maxSum);
    }
}
