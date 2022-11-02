import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        showDataTypes();
        int dataType = getDataType();
        if(dataType==1){
            int number = getNumber();
            int[] numbers=getNumbers(number);
            showCommonOperators();
            System.out.println("6 - Box plot");
            int operator = getOperator(dataType);
            lunch(numbers,operator);

        }else{
            // TODO: 11/2/2022
//            System.out.println("Enter w :");
//            int w=new Scanner(System.in).nextInt();
//            int number = getNumber();
//            int[] numbers=getNumbers(number);
//            int operator = getOperator(dataType);
//            lunch(numbers,operator);
        }


    }
    public static double findMean(int[] numbers){
        double sum=0;
        for(int i=0;i<numbers.length;i++){
            sum+=numbers[i];
        }
        return sum/numbers.length;
    }
    public static double findMedian(int[] numbers){
        numbers=sortNumbers(numbers);
        if(numbers.length%2==1){
            return numbers[numbers.length/2];
        }else{
           return (numbers[numbers.length/2-1]+numbers[numbers.length/2])/2.0;
        }

    }
    public static int[] sortNumbers(int[] numbers){
        Arrays.sort(numbers);
        return numbers;
    }

    // TODO: 11/2/2022
//    public static double findMode(int[] numbers){
//
//    }
    public static void lunch(int[] numbers,int operator){
        boolean doLoop=true;
        Scanner scanner=new Scanner(System.in);
        double answer=0;
        while (doLoop) {
            doLoop = false;
            switch (operator) {
                case 1:
                    answer=findMean(numbers);
                    break;
                case 2:
                    answer=findMedian(numbers);
                    break;
                case 3:
//                    answer=findMode(numbers);
                    break;
                case 4:

                    break;
                case 5:

                    break;
                case 6:

                    break;
                default:
                    showError();
                    doLoop = true;
            }
        }
        System.out.println(answer);
    }
    public static int[] getNumbers(int number){
        System.out.println("Enter your numbers : ");
        int[] numbers=new int[number];
        Scanner scanner=new Scanner(System.in);
        for(int i=0;i<number;i++){
            boolean doLoop=true;
            while(doLoop){
                doLoop=false;
                try{
                    numbers[i]=scanner.nextInt();
                }catch (Exception e){
                    showError();
                    doLoop=true;
                }
            }
        }
        return numbers;
    }

    public static void showError() {
        System.out.println("Wrong number try again!");
    }

    public static int getNumber() {
        System.out.println("Number of numbers :");
        Scanner scanner = new Scanner(System.in);
        int number = 0;
        boolean doLoop = true;
        while (doLoop) {
            doLoop = false;
            try {
                number = scanner.nextInt();
                if (number < 1) {
                    showError();
                    doLoop = true;
                }
            } catch (Exception e) {
                showError();
                doLoop = true;
            }

        }
        return number;
    }

    public static int getOperator(int dataType) {
        Scanner scanner = new Scanner(System.in);
        boolean doLoop = true;
        int operator = 0;
        while (doLoop) {
            doLoop = false;
            String input = scanner.next();
            switch (input) {
                case "1":
                    operator = 1;
                    break;
                case "2":
                    operator = 2;
                    break;
                case "3":
                    operator = 3;
                    break;
                case "4":
                    operator = 4;
                    break;
                case "5":
                    operator = 5;
                    break;
                case "6":
                    if(dataType==2){
                        showError();
                        doLoop=true;
                        break;
                    }
                    operator = 6;
                    break;
                default:
                    showError();
                    doLoop = true;
            }
        }
        return operator;
    }

    public static void showCommonOperators() {
        System.out.println("""
                Operators :
                1 - Mean
                2 - Median
                3 - Mode
                4 - Quantile
                5 - Variance""");
    }

    public static void showDataTypes() {
        System.out.println("Data type ?\n1 - Discrete\n2 - Continuous");
    }

    public static int getDataType() {
        Scanner scanner = new Scanner(System.in);
        boolean doLoop = true;
        int dataType = 0;
        while (doLoop) {
            doLoop = false;
            String input = scanner.next();
            if (input.equals("1")) {
                dataType = 1;
            } else if (input.equals("2")) {
                dataType = 2;
            } else {
                showError();
                doLoop = true;
            }
        }
        return dataType;
    }
}

