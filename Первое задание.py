#1
def result_after(score):
    if score >= 50:
        return "Зачёт"
    return "Незачёт"
#2
def print_cost_after(pages):
    if pages >= 10:
        return pages * 30 * 0.9
    return pages * 30
#3
def purchase_after(price, quantity):
    return price * quantity

balance = 5000 - purchase_after(700, 2)
print("Остаток:", balance)
#4
def fine_after(days):
    if days < 0:
        return "Ошибка"
    elif days <= 3:
        return 0
    return (days - 3) * 100
#5
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        if self.score >= 50:
            return "Зачёт"
        return "Незачёт"

class GrantStudent(Student):
    def get_result(self):
        if self.score >= 70:
            return "Грант сохранён"
        return "Грант не сохранён"