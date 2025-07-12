class Employee:
    def __init__(self, first_name, last_name, ann_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.ann_salary = ann_salary

    def bonus(self):
        return self.ann_salary * 0.1

E = Employee("Bethany", "Reed", 500)
print("Employee")
print("First name:", E.first_name)
print("Last name:", E.last_name)
print("Annual Salary: $%.2f"% E.ann_salary)
print("Bonus: $%.2f"% E.bonus())


class Manager(Employee):
    def bonus(self):
        return self.ann_salary * 0.2

    def long_bonus(self):
        return self.ann_salary * 0.5

M = Manager("Kevin", "Reed", 1000)
print()
print("Manager")
print("First name:", M.first_name)
print("Last name:", M.last_name)
print("Annual Salary: $%.2f"% M.ann_salary)
print("Bonus: $%.2f"% M.bonus())
print("Long term bonus: $%.2f"% M.long_bonus())
