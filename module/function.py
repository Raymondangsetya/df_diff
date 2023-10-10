import pandas as pd


def report_diff(new, old, key,report, debug=False):
    report = []  # Initialize the report list
    new_cols = set(new.columns)
    old_cols = set(old.columns)

    # Find deleted and new columns
    deleted_cols = list(old_cols - new_cols)
    new_added_cols = list(new_cols - old_cols)

    # Report deleted and new columns
    if deleted_cols:
        report_and_print(report, f"Deleted Columns on the new table: {', '.join(deleted_cols)}", debug)
    if new_added_cols:
        report_and_print(report, f"New Columns on the new table: {', '.join(new_added_cols)}", debug)

    common_cols = list(new_cols.intersection(old_cols) - {key})

    new_dict = {row[key]: row for _, row in new.iterrows()}
    old_dict = {row[key]: row for _, row in old.iterrows()}

    # Compare rows based on the key column
    for key_val in set(new_dict.keys()).union(old_dict.keys()):
        new_row = new_dict.get(key_val)
        old_row = old_dict.get(key_val)
        

        if new_row is not None and old_row is not None:
            for col in common_cols:
                new_val = new_row[col]
                old_val = old_row[col]
                if str(new_val).strip() != str(old_val).strip():
                    report_and_print(report, f"id: {key_val}-> {old_val} changed into {new_val} on column {col}", debug)
        elif new_row is not None:
            report_and_print(report, f"id: {key_val}-> is a new record on the new table", debug)
        else:
            report_and_print(report, f"id: {key_val}-> is removed on the new table", debug)

    return report

def report_and_print(the_list, text, debug):
    if debug:
        print(text)
    the_list.append(text)