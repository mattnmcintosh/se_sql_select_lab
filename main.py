# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd



# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)
print("---------------------First Five---------------------")
print(df_first_five)
print("-------------------End First Five-------------------")

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)
print("---------------------Five Reverse---------------------")
print(df_five_reverse)
print("-------------------End Five Reverse-------------------")

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber as ID FROM employees""", conn)
print("---------------------Alias---------------------")
print(df_alias)
print("-------------------End Alias-------------------")

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""SELECT *, CASE WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing" THEN "Executive" ELSE "Not Executive" END AS role FROM employees""", conn)
print("---------------------Executive---------------------")
print(df_executive)
print("-------------------End Executive-------------------")

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT length(lastName) as name_length FROM employees""", conn)
print("---------------------Name Length---------------------")
print(df_name_length)
print("-------------------End Name Length-------------------")

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT substr(jobTitle, 0, 3) as short_title FROM employees""", conn)
print("---------------------Short Title---------------------")
print(df_short_title)
print("-------------------End Short Title-------------------")

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""SELECT CAST(SUM(ROUND(priceEach*quantityOrdered, 0)) as INTEGER)  FROM orderDetails""", conn).iloc[:, 0]
print("---------------------Total Price---------------------")
print(sum_total_price)
print("-------------------End Total Price-------------------")

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""SELECT "Column not actually present" as orderDate, "06" as day, "" as month, "" as year FROM orderDetails""", conn)
print("---------------------Day Month Year---------------------")
print(df_day_month_year)
print("-------------------End Day Month Year-------------------")

conn.close()