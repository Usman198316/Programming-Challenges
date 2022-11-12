public class Task6 {
    private static int reverse(int num) {
        int reverse = 0;
        while (num >= 1) {
            int remainder = num % 10;
            reverse = reverse * 10 + remainder;
            num /= 10;
        }
        return reverse;
    }
    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]);
        int reversedNum = reverse(num1);
        System.out.println(reversedNum);
    }
}

