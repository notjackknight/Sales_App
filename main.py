from datetime import datetime
from Employee_Data import Job, Employee, employees, assign_lead, JobType


def greet():
    hour = datetime.now().hour
    greeting = (
        "Good morning!" if 5 <= hour < 12
        else "Good afternoon!" if 12 <= hour < 18
        else "Good evening!"
    )
    print(greeting)


def get_job_type():
    print("\nSelect a job type: ")
    for job in JobType:
        print(f"{job.value}. {job.name}")
    while True:
        try:
            choice = int(input("Please select a job type: "))
            return JobType(choice)
        except ValueError:
            print("Invalid choice. Please select an option between 1 and 5.")


greet()


def main():
    while True:
        print("\n--- Employee Performance System ---")
        print("1. Add New Employee")
        print("2. Update Job Performance")
        print("3. Display employee data")
        print("4. Assign Sales Lead")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

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
                job_type = get_job_type()
                sold = input("Was the job sold? (yes/no): ").lower() == 'yes'
                job = Job(job_type)
                employees[name].update_performance(job_type, sold)
                print(f"Performance updated for {name}")
            else:
                print(f"Employee {name} not found.")

        elif choice == '3':
            name = input("Enter employee name to display data: ")
            if name in employees:
                employees[name].display_info()
            else:
                print(f"Employee {name} not found.")

        elif choice == '4':
            job_type = get_job_type()
            assign_lead(job_type)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose a valid option.")

        while True:
            go_again = input("Do you want to keep working? (Yes/No): ").lower()
            if go_again == 'no':
                print("Thank you. Goodbye!")
                return
            elif go_again == 'yes':
                break
            else:
                print("You entered an invalid option. Please enter 'Yes' or 'No'.")


if __name__ == "__main__":
    main()
