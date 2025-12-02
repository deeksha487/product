import pytest

def employee_details(name, emp_id, department, salary):
    result = {
        "Employee Name": name,
        "Employee ID": emp_id,
        "Department": department,
        "Salary": salary
    }
    return result

if __name__ == "__main__":
    # sample input
    name = "Alice"
    emp_id = "E1001"
    department = "IT"
    salary = 55000

    print(employee_details(name, emp_id, department, salary))