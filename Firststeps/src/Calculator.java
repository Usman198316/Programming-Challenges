public class Calculator {
    private static int addition(int a, int b) {
        int answer = a + b;
        return answer;
    }
    private static int subtraction(int a, int b){
        int answer = a - b;
        return answer;
    }
    private static int multiplication(int a, int b){
        int answer = a * b;
        return answer;
    }
    private static double division(double a, double b) {
        double answer = a / b;
        return answer;
    }



    public static void main(String[] args){
        String choice = args[0];
        int value1 = Integer.parseInt(args[1]);
        int value2 = Integer.parseInt(args[2]);

        switch (choice) {
            case "addition":
                int added = addition(value1, value2);
                System.out.println(added);
                break;
            case "subtraction":
                int subtracted = subtraction(value1, value2);
                System.out.println(subtracted);
                break;
            case "multiplication":
                int multiplied = multiplication(value1, value2);
                System.out.println(multiplied);
                break;
            case "division":
                double divided = division(value1, value2);
                System.out.println(divided);
                break;
        }



    }
}

