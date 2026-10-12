from db_connection import create_connection


# 1. View all employees
def view_employees():
    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        print("\n========== EMPLOYEE DETAILS ==========")

        if employees:
            for employee in employees:
                print(employee)
        else:
            print("No employee records found.")

    except Exception as error:
        print("Error retrieving employees:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# 2. Add a new employee
def add_employee():
    print("\n========== ADD NEW EMPLOYEE ==========")

    name = input("Enter employee name: ").strip()
    email = input("Enter employee email: ").strip()
    department = input("Enter department: ").strip()
    salary = input("Enter salary: ").strip()
    joining_date = input("Enter joining date (YYYY-MM-DD): ").strip()

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO employees
            (employee_name, email, department, salary, joining_date)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (name, email, department, salary, joining_date)

        cursor.execute(query, values)
        connection.commit()

        print("Employee added successfully!")
        print("New Employee ID:", cursor.lastrowid)

    except Exception as error:
        connection.rollback()
        print("Error adding employee:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# 3. Search for an employee
def search_employee():
    print("\n========== SEARCH EMPLOYEE ==========")

    employee_id = input("Enter Employee ID to search: ").strip()

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            SELECT * FROM employees
            WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))
        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Found!")
            print("Employee ID:", employee[0])
            print("Name:", employee[1])
            print("Email:", employee[2])
            print("Department:", employee[3])
            print("Salary:", employee[4])
            print("Joining Date:", employee[5])
        else:
            print("No employee found with that ID.")

    except Exception as error:
        print("Error searching for employee:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# 4. Update employee details
def update_employee():
    print("\n========== UPDATE EMPLOYEE ==========")

    employee_id = input("Enter Employee ID to update: ").strip()

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Email")
    print("3. Department")
    print("4. Salary")

    choice = input("Choose an option (1-4): ").strip()

    fields = {
        "1": ("employee_name", "Enter new name: "),
        "2": ("email", "Enter new email: "),
        "3": ("department", "Enter new department: "),
        "4": ("salary", "Enter new salary: ")
    }

    if choice not in fields:
        print("Invalid choice!")
        return

    column, prompt = fields[choice]
    new_value = input(prompt).strip()

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = f"""
            UPDATE employees
            SET {column} = %s
            WHERE employee_id = %s
        """

        cursor.execute(query, (new_value, employee_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee details updated successfully!")
        else:
            print("Employee not found, or the details were unchanged.")

    except Exception as error:
        connection.rollback()
        print("Error updating employee:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# 5. Delete an employee
def delete_employee():
    print("\n========== DELETE EMPLOYEE ==========")

    employee_id = input("Enter Employee ID to delete: ").strip()

    confirmation = input(
        "Are you sure you want to delete this employee? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("Deletion cancelled.")
        return

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = "DELETE FROM employees WHERE employee_id = %s"

        cursor.execute(query, (employee_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    except Exception as error:
        connection.rollback()
        print("Error deleting employee:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# 6. Main menu
def main():
    while True:
        print("\n====================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("====================================")
        print("1. View All Employees")
        print("2. Add Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            view_employees()

        elif choice == "2":
            add_employee()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Thank you for using Employee Management System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


# Start the application
if __name__ == "__main__":
    main()