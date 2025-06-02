# 🛠️ Retail Data Engineering Assignment

Welcome to the **Retail Data Engineering** assignment!

This assignment simulates a simple **ETL (Extract, Transform, Load)** process using SQL and Python — without using Pandas or connecting to a database programmatically.

---

## 📦 Instructions

### 1. Clone this repository
```bash
git clone https://github.com/your-org/retail-data-engineering.git
cd retail-data-engineering
```

### 2. Create your branch
```bash
git checkout -b yourname-surname
```

---

## 📂 Assignment Tasks

### ✅ Task 1 – Extract (SQL)
- Open the SQL file at `sql/retail_data.sql` in [DB Browser for SQLite](https://sqlitebrowser.org/)
- Run the script to create and populate the database
- Write SQL queries to extract:
  - Top 5 customers by total amount spent
  - Number of orders per customer
  - Products that have never been ordered
- Export results as `.csv` into the `results/` folder:
  - `top_customers.csv`
  - `orders_per_customer.csv`
  - `unsold_products.csv`

---

### ✅ Task 2 – Transform (Python)
- Open `scripts/transform.py`
- Write a Python script that:
  - Loads `top_customers.csv`
  - Converts customer names to **title case**
  - Formats amounts into **₦ currency format** (e.g. ₦350,000.00)
  - Saves output to `top_customers_cleaned.csv` in the `results/` folder

---

### ✅ Task 3 – Load (Simulated)
- In the same script or new one (`load.py`), read `top_customers_cleaned.csv`
- Print each row like:
  ```
  Loading: Fatima Usman - ₦650,000.00
  ```

---

## 📤 Submit your work
```bash
git add .
git commit -m "Finished data engineering assignment"
git push origin yourname-surname
```
Then open a **Pull Request** on GitHub.

---

## 📁 Folder Structure

```
retail-data-engineering/
├── sql/
│   └── retail_data.sql
├── instructions/
│   └── README.md (this file)
├── tasks/
│   ├── task_1_extract.md
│   ├── task_2_transform.md
│   └── task_3_load.md
├── results/
│   └── (Your exported and cleaned CSVs go here)
├── scripts/
│   └── transform.py
└── .gitignore
```

Happy coding!
