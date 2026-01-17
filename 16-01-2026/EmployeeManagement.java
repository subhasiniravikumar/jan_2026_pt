import java.util.*;

class Employee {
    int id;
    String name;
    double salary;

    Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
}

public class EmployeeManagement {
    public static void main(String[] args) {
        ArrayList<Employee> list = new ArrayList<>();

        list.add(new Employee(101, "Anu", 45000));
        list.add(new Employee(102, "Kiran", 52000));

        for (Employee e : list) {
            System.out.println(e.id + " " + e.name + " " + e.salary);
        }
    }
}
