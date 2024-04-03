class Expense:

    def __init__(self, name, category, amount, date) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Amount: {self.amount}, Date: {self.date}"
    