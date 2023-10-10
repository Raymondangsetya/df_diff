

# Data Comparison and Reporting Tool

This Python script provides a data comparison and reporting tool to analyze differences between two Pandas DataFrames and generate a detailed report. It compares columns, rows, and key columns to identify changes, additions, and deletions in the data.

## Prerequisites

- Python 3.x
- Pandas library (`pip install pandas`)

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/data-comparison-tool.git
   cd df_diff
   ```

2. **Install Dependencies:**
   ```bash
   pip install pandas
   ```

3. **Usage:**
   - Import the necessary functions:
     ```python
     from data_comparison_tool import report_diff
     ```

   - Provide two Pandas DataFrames (`new` and `old`), a key column name (`key`), and a list to store the report (`Report`).

   - Call the `report_diff` function:
     ```python
     Report = report_diff(new=new, old=old, key='your_key_column', report=Report, debug=True)
     ```

   - Set `debug` to `True` if you want to print debug messages.

   - The function generates a detailed report in the `Report` list.

4. **Example:**
   ```python
   new_data = pd.DataFrame(...)  # Your new data
   old_data = pd.DataFrame(...)  # Your old data
   Report = []  # Initialize the report list
   Report = report_diff(new=new_data, old=old_data, key='id', report=Report, debug=True)
   print(Report)
   ```

## Report Format

The report contains information about deleted columns, new columns, changes in existing records, new records, and removed records.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this template according to your specific project details. Provide additional information, usage examples, and any other necessary details to help users understand and use your code effectively.
