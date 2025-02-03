import sqlite3


class BudgetManager:
    def __init__(self):
        self.conn = sqlite3.connect("expenses.db")
        self.create_table()
        self.total_budget = self.get_total_budget_from_db()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    amount REAL,
                    category TEXT
                )
            """
            )
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS budget (
                    id INTEGER PRIMARY KEY,
                    total_budget REAL
                )
            """
            )

    def set_total_budget(self, amount):
        self.total_budget = amount
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO budget (total_budget)
                VALUES (?)
            """,
                (amount,),
            )

    def get_total_budget_from_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT total_budget FROM budget ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        return result[0] if result else 0.0

    def is_budget_set(self):
        return self.total_budget > 0

    def add_expense(self, name, amount, category):
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO expenses (name, amount, category)
                VALUES (?, ?, ?)
            """,
                (name, amount, category),
            )

    def get_expenses(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, amount, category FROM expenses")
        return cursor.fetchall()

    def update_expense(self, expense_id, name, amount, category):
        with self.conn:
            self.conn.execute(
                """
                UPDATE expenses
                SET name = ?, amount = ?, category = ?
                WHERE id = ?
            """,
                (name, amount, category, expense_id),
            )

    def delete_expense(self, expense_id):
        with self.conn:
            self.conn.execute(
                """
                DELETE FROM expenses
                WHERE id = ?
            """,
                (expense_id,),
            )

    def get_remaining_budget(self):
        total_expenses = sum(expense[2] for expense in self.get_expenses())
        return self.total_budget - total_expenses

    def get_expenses_by_category(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        return dict(cursor.fetchall())
