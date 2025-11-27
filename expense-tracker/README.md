## 📊 Expense Tracker (Python)

A simple command-line Expense Tracker built in Python.
You can add expenses, view all expenses, see total summaries, and generate monthly spending reports.
All data is stored locally in a CSV file (expenses.csv).

This project demonstrates skills useful for:

✔ Python programming

✔ File handling

✔ CLI app design

✔ Basic data processing

✔ Clean, structured code

✔ Version control (Git/GitHub)

---

## 🚀 Features


✅ Add Expense

- Enter amount (€)
- Choose category (Food, Rent, Shopping, etc.)
- Optional note
- Automatically stored with today's date


🧾 View All Expenses

Displays every stored expense:

2025-02-15 | 12.50€ | Food | Lunch with friends


📈 Summary (Total + By Category)

Shows:
- Total money spent
- How much was spent per category

Example:

Total spent: 460.80€
- Food: 150.00€
- Rent: 250.00€
- Shopping: 60.80€

🗓 Monthly Summary

Enter a month like 2025-02, and the app will show:
- Total spending that month
- Category breakdown

---

## 📁 Project Structure

```markdown
expense-tracker/
│
├── app.py             # Main Python application
├── expenses.csv        # Stored expenses (auto-generated)
└── README.md           # Project documentation
```

---

## ▶️ How to Run

Make sure you have Python 3 installed.

Clone the repo:

```bash
git clone https://github.com/<your-username>/expense-tracker.git
```

Navigate into the folder:
```bash
cd expense-tracker
```

Run the app:
```bash
python app.py
```

---

## 🛠 Technologies Used

- Python 3
- Standard libraries: datetime, tabulate
- csv (if you add CSV module later)
- Git & GitHub for version control

---

## ✨ Future Improvements (Ideas)

Potential features to add later:

- Export monthly report to PDF or Excel
- Plot graphs (using matplotlib)
- Add edit/delete expense
- Switch to SQLite database
- Build a Tkinter GUI
- Convert the app into a web app (Flask / Django)

---

## 👤 Author

Uendi Faja – B.Sc. Computer Science student at TUHH, Hamburg
