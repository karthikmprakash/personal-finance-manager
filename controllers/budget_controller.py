from models.budget_manager import BudgetManager


class BudgetController:
    def __init__(self):
        self.budget_manager = BudgetManager()

    def set_total_budget(self, amount):
        self.budget_manager.set_total_budget(amount)

    def add_expense(self, name, amount, category):
        self.budget_manager.add_expense(name, amount, category)

    def get_expenses(self):
        return self.budget_manager.get_expenses()

    def update_expense(self, expense_id, name, amount, category):
        self.budget_manager.update_expense(expense_id, name, amount, category)

    def delete_expense(self, expense_id):
        self.budget_manager.delete_expense(expense_id)

    def get_remaining_budget(self):
        return self.budget_manager.get_remaining_budget()

    def get_expenses_by_category(self):
        return self.budget_manager.get_expenses_by_category()

    def is_budget_set(self):
        return self.budget_manager.is_budget_set()
