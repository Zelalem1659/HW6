CSCI HW6 – Python & MySQL Assignment
====================================

This project contains a Python program (`hw6_app.py`) that performs all 
required database operations for Homework 6 using MySQL.

Video Demonstration:
https://youtu.be/bH8eoXZ1rUw


---------------------------------------------------------
Assignment Requirements
---------------------------------------------------------
The program implements all required tasks:

1. Insert the tuple ('s2', 'p3', 200, 0.006) into the SHIPMENT table 
   and report Success or Fail.

2. Insert the tuple ('s4', 'p2', 100, 0.005) into the SHIPMENT table 
   and report Success or Fail.

3. Increase the status of each supplier by 10%.

4. Display all suppliers from the SUPPLIER table.

5. Prompt the user for a part number (pno) and display all suppliers 
   who shipped that part using a parameterized SQL query (safe from 
   SQL injection).


---------------------------------------------------------
Important Note
---------------------------------------------------------
The database (`supplierpartsdb`) and its tables (SUPPLIER, PART, SHIPMENT) 
already existed on my local MySQL Workbench from previous assignments 
(HW4 and HW5).  

For completeness, the SQL commands to recreate the tables are included 
below so another user could reproduce the environment if needed.  
However, during development and recording of the video, I used my 
existing local database.


---------------------------------------------------------
Setup Instructions
---------------------------------------------------------

1. Install Python
   - Download Python from: https://www.python.org/downloads/
   - During installation, enable: **“Add Python to PATH”**

2. Install MySQL Connector for Python
   Open Command Prompt or PowerShell and run:
       pip install mysql-connector-python

3. Configure Database Connection inside `hw6_app.py`
   Update the following section with your own MySQL credentials:

       connection = mysql.connector.connect(
           host="localhost",
           user="root",
           password="YOUR_PASSWORD",
           database="supplierpartsdb"
       )

4. (Optional) Create the Database and Tables
   Only needed if database does not already exist.
   Run in MySQL Workbench:

       CREATE DATABASE supplierpartsdb;
       USE supplierpartsdb;

       CREATE TABLE SUPPLIER (
           sno VARCHAR(10) PRIMARY KEY,
           sname VARCHAR(50),
           status INT,
           city VARCHAR(50)
       );

       CREATE TABLE PART (
           pno VARCHAR(10) PRIMARY KEY,
           pname VARCHAR(50),
           color VARCHAR(20),
           weight FLOAT,
           city VARCHAR(50)
       );

       CREATE TABLE SHIPMENT (
           sno VARCHAR(10),
           pno VARCHAR(10),
           qty INT,
           price FLOAT,
           PRIMARY KEY (sno, pno),
           FOREIGN KEY (sno) REFERENCES SUPPLIER(sno),
           FOREIGN KEY (pno) REFERENCES PART(pno)
       );

5. Run the Program
   - Navigate to the HW6 directory in terminal:
         cd "path_to/HW6/HW6"

   - Run:
         python hw6_app.py


---------------------------------------------------------
What Each Task Does
---------------------------------------------------------

• Task 1  
  Inserts ('s2','p3',200,0.006) into SHIPMENT and reports success or error.

• Task 2  
  Inserts ('s4','p2',100,0.005) into SHIPMENT and reports success or error.

• Task 3  
  Increases supplier statuses by 10%.

• Task 4  
  Displays all suppliers from the SUPPLIER table.

• Task 5  
  Asks for a part number and displays suppliers who shipped that part, 
  using a safe parameterized SQL query.


---------------------------------------------------------
Notes
---------------------------------------------------------
• Ensure your MySQL server is running before executing the program.  
• If you encounter connection issues, verify your username, password, 
  and database name inside `hw6_app.py`.  
• The video demonstrates the program execution as required in HW6.  
