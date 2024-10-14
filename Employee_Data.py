from enum import Enum


class JobType(Enum):
    CRAWLSPACE = 1
    FOUNDATION = 2
    BASEMENT = 3
    POLY = 4
    MISC = 5


class Job:
    def __init__(self, job_type):
        if isinstance(job_type, JobType):
            self.job_type = job_type
        else:
            raise ValueError("Invalid job type")


class Employee:

    def __init__(self, name):
        self.name = name
        self.performance = {}

    def update_performance(self, job_type, sold):
        if job_type not in self.performance:
            self.performance[job_type] = {'successes': 0, 'attempts': 0}
        self.performance[job_type]['attempts'] += 1
        if sold:
            self.performance[job_type]['successes'] += 1

    def get_success_rate(self, job_type):
        if job_type in self.performance:
            attempts = self.performance[job_type]['attempts']
            successes = self.performance[job_type]['successes']
            return successes / attempts if attempts > 0 else 0
        return 0

    def get_overall_success_rate(self):
        total_successes = sum(data['successes'] for data in self.performance.values())
        total_attempts = sum(data['attempts'] for data in self.performance.values())
        if total_attempts > 0:
            return total_successes/total_attempts
        return 0

    def display_info(self):
        print(f"\nEmployee Name: {self.name}")
        print("Performance Data: ")
        if not self.performance:
            print("No performance data available.")
            return
        for job_type, data in self.performance.items():
            success_rate = self.get_success_rate(job_type)
            print(f"Job type: {job_type.name}")
            print(f"    Successes: {data['successes']}")
            print(f"    Attempts: {data['attempts']}")
            print(f"    Success Rate: {success_rate:.2%}")

        overall_success_rate = self.get_overall_success_rate()
        print(f"\nOverall Success Rate: {overall_success_rate:.2%}")


employees = {}


def assign_lead(job_type):
    best_success_rate = -1
    best_lead = None

    for employee in employees.values():
        if job_type in employee.performance:
            success_rate = employee.get_success_rate(job_type)
            if success_rate > best_success_rate:
                best_success_rate = success_rate
                best_lead = employee

    if best_lead:
        print(f"\n{best_lead.name} has been assigned to this job.")
        print(f"Their success rate for this job type is: {best_success_rate * 100:.2f}%")
    else:
        print("No suitable lead found for this job type.")
