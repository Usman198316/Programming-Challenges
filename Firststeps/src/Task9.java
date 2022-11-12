public class Task9 {
    public static void main(String[] args) {
        System.out.println(1);
        for (int i = 100; i <= 999; i ++) {
            int digit1 = i % 10;
            int digit2 = (i / 10) % 10;
            int digit3 = (i / 100) % 10;
            double sumCubes = Math.pow(digit1, 3) + Math.pow(digit2, 3) + Math.pow(digit3, 3);
            if (sumCubes == i) {
                System.out.println(i);
            }
        }
    }
}
