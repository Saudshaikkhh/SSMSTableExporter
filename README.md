# TableExporter 🚀

**TableExporter** is a Python script that connects to a SQL Server database, retrieves the names of all tables, and exports them to both a **text file** and an **Excel file**. It’s a handy tool for database administrators and developers who need to quickly document or analyze database schemas.

### Why Use TableExporter?
- **Efficiency**: Automates the process of fetching and exporting table names, saving you time and effort.
- **Flexibility**: Exports data to both `.txt` and `.xlsx` files, catering to different use cases.
- **Ease of Use**: Simple configuration and execution make it accessible for users of all skill levels.
- **Lightweight**: Built with `pyodbc` and `pandas`, ensuring fast and reliable performance.

### Key Features ✨
- **Database Connectivity**: Connects to SQL Server using `pyodbc`.
- **Table Name Extraction**: Retrieves all table names from the specified database.
- **Dual Export**: Exports table names to both a text file (`table_names.txt`) and an Excel file (`table_names.xlsx`).
- **Customizable**: Easily configure database connection details in the script.

### Use Cases
- **Database Documentation**: Quickly generate a list of tables for documentation purposes.
- **Schema Analysis**: Analyze database schemas by exporting table names for further processing.
- **Onboarding**: Help new team members understand the database structure.

---

## Prerequisites 📋

Before using **TableExporter**, ensure you have the following installed:

- **Python 3.7+**
- **pyodbc**: For connecting to SQL Server.
- **pandas**: For exporting data to Excel.

You can install the required libraries using:

```bash
pip install pyodbc pandas
```

---
#Usage 🛠️
1. Clone the Repository:
```bash
git clone https://github.com/your-username/TableExporter.git
cd TableExporter
```
2. Update Configuration:
Open the script (table_exporter.py) and update the following variables with your database details:
```python
server = 'your_server_address,port'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
```

3. Run the Script:
Execute the script using Python:
```bash
python table_exporter.py
```
4. Check Output:
The table names will be saved in table_names.txt.
An Excel file named table_names.xlsx will also be created.
Example Output 📂
```
Text File (table_names.txt):
customers
orders
products
Excel File (table_names.xlsx):
Table Name
customers
orders
products
```
---
#Contributing 🤝
Contributions are welcome! If you'd like to improve TableExporter, follow these steps:

-Fork the repository.

-Create a new branch (git checkout -b feature/YourFeatureName).

-Commit your changes (git commit -m 'Add some feature').

-Push to the branch (git push origin feature/YourFeatureName).

-Open a pull request.
---
#License 📜:
```
This project is licensed under the MIT License. See the LICENSE file for details.
```
---
#Support 💖
```
If you find this project helpful, consider giving it a ⭐️ on GitHub! For any questions or issues, feel free to open an issue.
Happy Coding! 🎉
```