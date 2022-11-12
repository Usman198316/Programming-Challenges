public class Task8 {
    private static int HCF(int num1, int num2) {
        int HCF = 0;
        if (num1 > num2) {
            for (int i = 1; i <= num2; i++) {
                if ((num1 % i == 0) && (num2 % i == 0)) {
                    HCF = i;
                }
            }
        }
        if (num1 < num2) {
            for (int i = 1; i <= num1; i++) {
                if ((num1 % i == 0) && (num2 % i == 0)) {
                    HCF = i;
                }
            }
        }
        return HCF;
    }

    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]), num2 = Integer.parseInt(args[1]);
        int HCF = HCF(num1, num2);
        System.out.println(HCF);
    }
}
