# Author :- Biresashis Das

# Here we will see how to create a Table using prettytable module

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("CAR BRAND", ["TATA", "MAHINDRA XUV700", "JAGUAR",])
table.add_column("OWNER NAME", ["SIR RATAN TATA", "Mr. ANAND MAHINDRA", "SIR RATAN TATA",])
table.align = "l"
print(table)


# It will show the given output

#       +-----------------+--------------------+
#       | CAR BRAND       | OWNER NAME         |
#       +-----------------+--------------------+
#       | TATA            | SIR RATAN TATA     |
#       | MAHINDRA XUV700 | Mr. ANAND MAHINDRA |
#       | JAGUAR          | SIR RATAN TATA     |
#       +-----------------+--------------------+
