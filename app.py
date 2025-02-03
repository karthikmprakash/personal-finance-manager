import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Ensure the budget_controller module is in the same directory
from controllers.budget_controller import BudgetController

# Initialize BudgetController
budget_controller = BudgetController()

# Load expenses from the database on startup
expenses = budget_controller.get_expenses()

# Streamlit UI
st.title("Personal Finance Manager")

# Input for total budget
if not budget_controller.is_budget_set():
    total_budget = st.number_input(
        "Enter your total budget for the month (₹):", min_value=0.0, step=0.01
    )
    if total_budget:
        budget_controller.set_total_budget(total_budget)
        st.rerun()
else:
    st.write(
        f"Total budget for the month is already set to ₹{budget_controller.budget_manager.total_budget}"
    )
    if st.button("Edit Budget"):
        new_total_budget = st.number_input(
            "Enter new total budget for the month (₹):",
            min_value=0.0,
            step=0.01,
            value=budget_controller.budget_manager.total_budget,
        )
        if st.button("Update Budget"):
            budget_controller.update_total_budget(new_total_budget)
            st.success(f"Updated total budget to ₹{new_total_budget}")
            st.rerun()

# Input for adding expenses
expense_name = st.text_input("Enter expense name:")
expense_amount = st.number_input("Enter expense amount (₹):", min_value=0.0, step=0.01)
expense_category = st.selectbox(
    "Select expense category:",
    [
        "Food",
        "Transport",
        "Entertainment",
        "Utilities",
        "Rent",
        "Healthcare",
        "Insurance",
        "Savings",
        "Education",
        "Miscellaneous",
        "Loan",
    ],
)

if st.button("Add Expense"):
    if expense_name and expense_amount:
        budget_controller.add_expense(expense_name, expense_amount, expense_category)
        st.success(
            f"Added expense: {expense_name} - ₹{expense_amount} ({expense_category})"
        )
    else:
        st.error("Please enter all expense details.")

# Display expenses
st.subheader("Expenses")
expenses = budget_controller.get_expenses()
expense_df = pd.DataFrame(expenses, columns=["ID", "Name", "Amount", "Category"])

# Add a checkbox for each expense inside the table
selected_expenses = []
for index, row in expense_df.iterrows():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.write(row["ID"])
    col2.write(row["Name"])
    col3.write(row["Amount"])
    col4.write(row["Category"])
    selected = col5.checkbox("Select", key=row["ID"])
    if selected:
        selected_expenses.append(row["ID"])

# Add a single delete button to delete selected expenses
if st.button("Delete Selected Expenses"):
    for expense_id in selected_expenses:
        budget_controller.delete_expense(expense_id)
    st.success(f"Deleted selected expenses: {selected_expenses}")
    st.rerun()

# Display the table
st.dataframe(expense_df)

# Input for updating expenses
st.subheader("Update Expense")
expense_id = st.number_input("Enter expense ID to update:", min_value=1, step=1)
new_expense_name = st.text_input("Enter new expense name:")
new_expense_amount = st.number_input(
    "Enter new expense amount (₹):", min_value=0.0, step=0.01
)
new_expense_category = st.selectbox(
    "Select new expense category:",
    [
        "Food",
        "Transport",
        "Entertainment",
        "Utilities",
        "Rent",
        "Healthcare",
        "Insurance",
        "Savings",
        "Education",
        "Miscellaneous",
    ],
)

if st.button("Update Expense"):
    if new_expense_name and new_expense_amount:
        budget_controller.update_expense(
            expense_id, new_expense_name, new_expense_amount, new_expense_category
        )
        st.success(
            f"Updated expense ID {expense_id}: {new_expense_name} - ₹{new_expense_amount} ({new_expense_category})"
        )
    else:
        st.error("Please enter all new expense details.")

# Input for deleting expenses
st.subheader("Delete Expense")
delete_expense_id = st.number_input("Enter expense ID to delete:", min_value=1, step=1)

if st.button("Delete Expense"):
    budget_controller.delete_expense(delete_expense_id)
    st.success(f"Deleted expense ID {delete_expense_id}")

# Display remaining budget
remaining_budget = budget_controller.get_remaining_budget()
st.subheader(f"Remaining Budget: ₹{remaining_budget}")

# Display expenses by category
st.subheader("Expenses by Category")
expenses_by_category = budget_controller.get_expenses_by_category()
expenses_by_category_df = pd.DataFrame(
    list(expenses_by_category.items()), columns=["Category", "Amount"]
)
st.bar_chart(expenses_by_category_df.set_index("Category"))

# Display pie charts side by side
st.subheader("Expense Distribution")
col1, col2 = st.columns(2)

with col1:
    st.write("By Category")
    fig, ax = plt.subplots()
    expenses_by_category["Remaining Budget"] = remaining_budget
    ax.pie(
        expenses_by_category.values(),
        labels=expenses_by_category.keys(),
        autopct="%1.1f%%",
    )
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

with col2:
    st.write("By Name")
    expenses_by_name = {expense[1]: expense[2] for expense in expenses}
    expenses_by_name["Remaining Budget"] = remaining_budget
    fig, ax = plt.subplots()
    ax.pie(expenses_by_name.values(), labels=expenses_by_name.keys(), autopct="%1.1f%%")
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
