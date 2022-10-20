public class Tasks2 {
    public static void main(String[] args){
        for_loop();
        create_car_list();
        integer_days();
        switch_days();
        catch_list_error();
    }

    public static void for_loop(){
        for(int i = 0; i < 5; i++){
            System.out.println("Yes");
        }
    }

    public static void create_car_list(){
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for(String car : cars){
            System.out.println(car);
        }
    }

    public static void integer_days(){
        int day = 4;
        if (day == 6){
            System.out.println("Today is Saturday ");
        }
        else if (day == 7){
            System.out.println("Today is Sunday ");
        }
        else{
            System.out.println("Looking forward to the weekend");
        }
    }

    public static void switch_days(){
        int day = 4;
        switch(day){
            case 7:
                System.out.println("Today is Sunday");
                break;
            case 6:
                System.out.println("Today is Saturday");
                break;
            default:
                System.out.println("Looking forward to the weekend");
        }
    }

    public static void catch_list_error(){
        int[] myNumbers = {1,3,3};
        try{
            System.out.println(myNumbers[9]);
        } catch (Exception e){
        System.out.println("That is not in the list (array index out of bounds)");
    }
}}

