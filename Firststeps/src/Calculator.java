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

    private static double square(double a){
        double answer = Math.pow(a, 2);
        return answer;
    }

    private static double cube(double a){
        double answer = Math.pow(a, 3);
        return answer;
    }

    private static double pow(double a, double b){
        double answer = Math.pow(a, b);
        return answer;
    }

    private static double factorial(double a){
        double answer = 1;
        for(int i = 1; i <= a; answer *= i++);
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
            case "square":
                double squared = square(value1);
                System.out.println(squared);
                break;
            case "cube":
                double cubed = cube(value1);
                System.out.println(cubed);
                break;
            case "power":
                double powerOf = pow(value1, value2);
                System.out.println(powerOf);
                break;
            case "factorial":
                double fact = factorial(value1);
                System.out.println(fact);
                break;
        }



    }
}
