import java.util.Scanner;

class Salary {
    double gross, tax_amount, net;

    // Constructor with values
    Salary(double g) {
        gross = g;
    }

    // Default constructor
    Salary() {
        gross = 0;
        tax_amount = 0;
        net = 0;
    }

    void data_in() {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter gross salary: ");
        gross = in.nextDouble();
    }

    void compute() {
        if (gross >= 30000)
            tax_amount = gross * 0.15;
        else if (gross >= 20000)
            tax_amount = gross * 0.12;
        else if (gross >= 10000)
            tax_amount = gross * 0.10;
        else
            tax_amount = 0;

        net = gross - tax_amount;
    }

    void data_out() {
        System.out.println("Tax Amount = " + tax_amount);
        System.out.println("Net Salary = " + net);
    }
}

public class SalaryTest {
    public static void main(String[] args) {
        Salary s = new Salary();
        s.data_in();
        s.compute();
        s.data_out();
    }
}
