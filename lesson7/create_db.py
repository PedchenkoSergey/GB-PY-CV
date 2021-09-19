import sqlite3
import os


def database_creation():
    db_path = os.path.join('.', 'dbls7.sqlite')
    # print(db_path)
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    # Create additional tables
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS categories (
        category_name TEXT NOT NULL,
        category_description TEXT NOT NULL,
        PRIMARY KEY (category_name)
        );
        
        CREATE TABLE IF NOT EXISTS units(
        unit TEXT NOT NULL,
        PRIMARY KEY (unit)
        );
        
        CREATE TABLE IF NOT EXISTS positions (
        position TEXT NOT NULL,
        PRIMARY KEY (position)
        );
    """)

    conn.commit()

    # Create main tables:
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS goods (
        good_id INTEGER NOT NULL,
        good_name TEXT NOT NULL,
        good_unit TEXT NOT NULL,
        good_cat TEXT NOT NULL,
        PRIMARY KEY (good_id),
        FOREIGN KEY (good_unit) REFERENCES units(unit) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (good_cat) REFERENCES categories(category_name) ON DELETE CASCADE ON UPDATE CASCADE
        );
        
        CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER NOT NULL,
        employee_fio TEXT NOT NULL,
        employee_position TEXT NOT NULL,
        PRIMARY KEY (employee_id),
        FOREIGN KEY (employee_position) REFERENCES positions(position) ON DELETE CASCADE ON UPDATE CASCADE 
        );
        
        CREATE TABLE IF NOT EXISTS vendors (
        vendor_id INTEGER NOT NULL,
        vendor_name TEXT NOT NULL, 
        vendor_ownerchipform TEXT NOT NULL, 
        vendor_address TEXT NOT NULL, 
        vendor_phone TEXT NOT NULL, 
        vendor_email TEXT NOT NULL,
        PRIMARY KEY (vendor_id)
        );
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    database_creation()
