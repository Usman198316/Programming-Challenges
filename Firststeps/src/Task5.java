import static java.lang.Integer.parseInt;

public class Task5 {
    public static void main(String[] args) {
        double num1 = Integer.parseInt(args[0]), num2 = Integer.parseInt(args[1]);
        double result = Math.pow(num1, num2);
        System.out.println(result);

    }
}
