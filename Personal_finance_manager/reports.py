from config import get_budget
from database import get_total_expense

def get_remaining_budget():

    total_budget = get_budget()
    total_expenses = get_total_expense()

    remaining_budget = total_budget - total_expenses

    return remaining_budget


