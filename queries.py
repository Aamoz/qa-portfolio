import sqlite3

conn = sqlite3.connect('synergy_practice.db')
c = conn.cursor()

print("=== All Patients ===")
c.execute("SELECT * FROM patients")
for row in c.fetchall():
    print(row)

print("\n=== Nut-free Patients ===")
c.execute("SELECT * FROM patients WHERE dietary_requirement = 'Nut-free'")
for row in c.fetchall():
    print(row)

print("\n=== Confirmed Orders Count ===")
c.execute("SELECT COUNT(*) FROM orders WHERE status = 'Confirmed'")
print(c.fetchone()[0])

print("\n=== Patient Orders (JOIN) ===")
c.execute("""SELECT patients.patient_name, orders.meal, orders.status 
             FROM orders 
             INNER JOIN patients ON orders.patient_id = patients.patient_id""")
for row in c.fetchall():
    print(row)

print("\n=== Nut-free Patient Orders (Data Validation) ===")
c.execute("""SELECT patients.patient_name, patients.dietary_requirement, orders.meal, orders.status 
             FROM orders 
             INNER JOIN patients ON orders.patient_id = patients.patient_id 
             WHERE patients.dietary_requirement = 'Nut-free'""")
for row in c.fetchall():
    print(row)

print("\n=== Duplicate Orders (Bug Detection) ===")
c.execute("""SELECT patient_id, meal, COUNT(*) as order_count 
             FROM orders 
             GROUP BY patient_id, meal 
             HAVING COUNT(*) > 1""")
for row in c.fetchall():
    print(row)

conn.close()