# 🏢 Enterprise Design Pattern: Table Module (Python)

This repository demonstrates the **Table Module** pattern from *Martin Fowler’s* *Catalog of Enterprise Application Architecture* using a simple **Orders** system built in Python.  

---

## 📦 Project Structure
```
enterprise-table-module/
├─ table_module.py       # Main Table Module implementation
├─ tests/
│   └─ test_table_module.py
├─ requirements.txt
└─ .github/workflows/
   └─ ci.yml
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/enterprise-table-module.git
cd enterprise-table-module
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the demo
```bash
python table_module.py
```

---

## ✅ Run Tests
```bash
pytest -v
```

---

## 🤖 CI/CD Automation
This project includes **GitHub Actions**:

- Runs tests automatically on every `push` or `pull request`.
- Ensures your code is always working before merging.

File: `.github/workflows/ci.yml`

---

## 🎯 Example Output
```bash
💰 Total Sales: 245.5
🛒 Alice Sales: 165.0
```

---

## 📚 References
- Pattern: **Table Module**  
- Source: *Patterns of Enterprise Application Architecture* by Martin Fowler  

---

✨ Feel free to fork, test, and adapt this pattern to your own enterprise applications!
