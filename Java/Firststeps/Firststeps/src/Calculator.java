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
    private static double division(int a, int b) {
        double answer = a / b;
        return answer;
    }



    public static void main(String[] args){
        String choice = args[0];

        switch (choice) {
            case "addition":
        }
        int value1 = Integer.parseInt(args[1]);
        int value2 = Integer.parseInt(args[2]);
        int add = addition(value1, value2);
        int subtract = subtraction(value1, value2);
        int multiply = multiplication(value1, value2);
        double divide = division(value1, value2);
        System.out.println(multiply);

    }
}

