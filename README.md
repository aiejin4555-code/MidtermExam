# Weekly Expense Logger
**Kassandra Faye Llagas | BSIT SE 1A**

A Python console application that allows a student to log up to 5 weekly expenses across predefined spending categories and view a formatted summary report.

---

## Features

- Input validation with descriptive error messages for all user entries
- Five predefined expense categories with real-world examples displayed in the menu
- Up to 5 expense entries per session, with the option to skip any slot
- Automatic **High Expense Alert** flag when a single expense exceeds 25% of the weekly budget
- Clean formatted report showing itemized expenses, total spent, remaining balance, and budget status
- Expenses stored as dictionaries for organized data handling
- Uses **f-strings** for output formatting (no `.2f` decimal formatting)


---

## Usage Walkthrough

**Step 1 — Enter your name and weekly budget**
```
Student name: Kassandra Faye Llagas
Weekly budget: 1000
```

**Step 2 — View the category menu**
```
==========================================
    WEEKLY EXPENSE -- CATEGORIES
==========================================
 1. Food & Drinks        [e.g. Lunch, snacks, coffee]
 2. Transportation       [e.g. Bus, jeepney, ride-share]
 3. Mobile / Internet    [e.g. Load, data plan, WiFi top-up]
 4. School Supplies      [e.g. Notebook, pen, bond paper]
 5. Entertainment        [e.g. Games, movies, hangout]
==========================================
```

**Step 3 — Log up to 5 expenses**

For each expense slot, you will be prompted to enter:
- A category number (1–5), or `0` to skip the slot
- A short description
- The amount spent

**Step 4 — View the summary report**

The program prints a formatted report with all logged expenses, total spending, remaining balance, and a budget status message.

---

## Sample Output

```
======================================================
      KASSANDRA FAYE LLAGAS -- WEEKLY EXPENSE LOG
======================================================
  Weekly Budget  : P1000.0
  [1] Food & Drinks
      Jollibee lunch P350.0   [High Expense Alert!]
  [2] Transportation
      Jeepney fare P50.0
  [3] School Supplies
      Notebook and pen P120.0
------------------------------------------------------
  Total Spent    : P520.0
  Remaining      : P480.0
  Status         : Budget OK. Keep it up!
======================================================
```

## Author

Kassandra Faye Llagas
BSIT SE 1A — Software Engineering
