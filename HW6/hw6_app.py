import mysql.connector
from mysql.connector import Error

# --------------------------------------------
# Function to connect to MySQL
# --------------------------------------------
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Beletshachew1972",   # <-- Use your MySQL password
            database="supplierpartsdb"     # <-- Your database name
        )
        if connection.is_connected():
            print("Connected to MySQL successfully!")
            return connection
    except Error as e:
        print(f"Error connecting: {e}")
        return None


# --------------------------------------------
# TASK 1: Insert REQUIRED tuple ('s2','p3',200,0.006)
# --------------------------------------------
def task1_insert_row(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO shipment (sno, pno, qty, price)
            VALUES ('s2', 'p3', 200, 0.006)
        """)
        conn.commit()
        print("\nTask 1 complete: Row ('s2','p3',200,0.006) inserted.")
    except Error as e:
        print(f"Task 1 failed: {e}")


# --------------------------------------------
# TASK 2: Insert REQUIRED tuple ('s4','p2',100,0.005)
# --------------------------------------------
def task2_insert_param(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO shipment (sno, pno, qty, price)
            VALUES ('s4', 'p2', 100, 0.005)
        """)
        conn.commit()
        print("\nTask 2 complete: Row ('s4','p2',100,0.005) inserted.")
    except Error as e:
        print(f"Task 2 failed: {e}")


# --------------------------------------------
# TASK 3: Increase supplier status by 10%
# --------------------------------------------
def task3_increase_status(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE supplier
            SET status = status * 1.10
        """)
        conn.commit()
        print("\nTask 3 complete: Supplier status increased by 10%.")
    except Error as e:
        print(f"Task 3 failed: {e}")


# --------------------------------------------
# TASK 4: Display all suppliers
# --------------------------------------------
def task4_show_suppliers(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM supplier")
        rows = cursor.fetchall()

        print("\nTask 4 — Supplier Table:")
        print("---------------------------------------")
        for row in rows:
            print(row)
        print("---------------------------------------")
    except Error as e:
        print(f"Task 4 failed: {e}")


# --------------------------------------------
# TASK 5: Ask user for part number & show matching parts
# Safe SQL (prevents injection)
# --------------------------------------------
def task5_search_part(conn):
    try:
        cursor = conn.cursor()
        pno = input("\nTask 5 — Enter part number to search (ex: p1): ").strip()

        cursor.execute("SELECT * FROM part WHERE pno = %s", (pno,))
        rows = cursor.fetchall()

        if not rows:
            print("No part found with that Pno.")
        else:
            print("\nPart details:")
            for row in rows:
                print(row)

    except Error as e:
        print(f"Task 5 failed: {e}")


# --------------------------------------------
# MAIN PROGRAM  
# --------------------------------------------
def main():
    conn = create_connection()
    if conn is None:
        return

    while True:
        print("\n===== HW6 MENU =====")
        print("1. Insert required tuple (Task 1)")
        print("2. Insert second required tuple (Task 2)")
        print("3. Increase supplier status by 10% (Task 3)")
        print("4. Show all suppliers (Task 4)")
        print("5. Search for part by number (Task 5)")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            task1_insert_row(conn)
        elif choice == "2":
            task2_insert_param(conn)
        elif choice == "3":
            task3_increase_status(conn)
        elif choice == "4":
            task4_show_suppliers(conn)
        elif choice == "5":
            task5_search_part(conn)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

    conn.close()


# Run program
if __name__ == "__main__":
    main()
