from datetime import datetime
from Employee_Data import Job, Employee, employees, assign_lead


def greet():
    hour = datetime.now().hour
    greeting = (
        "Good morning!" if 5 <= hour < 12
        else "Good afternoon!" if 12 <= hour < 18
        else "Good evening!"
    )
    print(greeting)


greet()


def main():
    while True:
        print("\n--- Employee Performance System ---")
        print("1. Add New Employee")
        print("2. Update Job Performance")
        print("3. Display employee data")
        print("4. Assign Sales Lead")
        print("5. Exit")
        print("")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            name = input("Enter employee name: ")
            if name not in employees:
                employees[name] = Employee(name)
                print(f"{name} has been added to your employee list.")
            else:
                print(f"Employee {name} already exists.")

        elif choice == '2':
            name = input("Enter employee name: ")
            if name in employees:
                job_type = input("Enter job type: ")
                sold = input("Was the job sold? (yes/no): ").lower() == 'yes'
                job = Job(job_type)
                employees[name].update_performance(job.job_type, sold)
                print(f"Performance update for {name}")
            else:
                print(f"Employee {name} not found.")

        elif choice == '3':
            name = input("Enter employee name to display data: ")
            if name in employees:
                employees[name].display_info()
                overall_rate = employees[name].get_overall_success_rate()
                print(f"Overall success rate for {name}: {overall_rate:.2f}")
            else:
                print(f"Employee {name} not found.")

        elif choice == '4':
            input("Enter the job type: ")
            assign_lead(job_type)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose a valid option.")

        go_again = input("Do you want to keep working? (yes/no):").lower()
        if go_again != 'yes':
            print("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
