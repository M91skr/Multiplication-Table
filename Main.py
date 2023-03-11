"""---------------------------------------- Multiplication Table (With prettytable) ----------------------------------------

In this code, a simple multiplication table is created using prettytable.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

from prettytable import PrettyTable

# ---------------------------------------- Get Table Scale ----------------------------------------

num = int(input('What is the size of the multiplication table? 10*(10, 11, ...)\n'))

# ---------------------------------------- Building the first column ----------------------------------------
table = PrettyTable()
table.add_column("Multiplication table", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# ---------------------------------------- Building other columns ----------------------------------------

for i in range(0, num+1):
    lst_1 = []
    for j in range(0, 11):
        lst_1.append(i * j)
    table.add_column(str(i), lst_1)

# ---------------------------------------- Display Output ----------------------------------------

print(table)