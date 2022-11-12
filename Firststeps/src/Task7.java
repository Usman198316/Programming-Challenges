public class Task7 {
    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]);
        double factors = 0;
        if (num1 == 1) {
            System.out.println("1 is not prime");
        } else {
            for (double i = 2; i < num1; i++) {
                if (num1 % i == 0) {
                    factors += 1;
                }

            }
            if (factors == 0) {
                System.out.printf("%d is prime", num1);

            } else {
                System.out.printf("%d is not prime", num1);
            }

        }

    }
}
