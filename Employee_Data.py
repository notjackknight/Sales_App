class Job:
    def __init__(self, job_type):
        self.job_type = job_type


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
        total_successes = 0
        total_attempts = 0
        for data in self.performance.values():
            total_successes += data['successes']
            total_attempts += data['attempts']
        if total_attempts == 0:
            return 0
        return total_successes / total_attempts

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print("Performance Data: ")
        if not self.performance:
            print("No performance data available.")
            return
        for job_type, data in self.performance.items():
            success_rate = self.get_success_rate(job_type)
            print(f"Job type: {job_type}")
            print(f"    Successes: {data['successes']}")
            print(f"    Attempts: {data['attempts']}")
            print(f"    Success Rate: {success_rate:,.2%}")

        overall_success_rate = self.get_overall_success_rate()
        print(f"Overall Success Rate: {overall_success_rate:.2%}\n")