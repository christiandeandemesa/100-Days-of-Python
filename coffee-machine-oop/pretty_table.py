# Installed the python package using: pip install PrettyTable from https://pypi.org/project/prettytable/.
from prettytable import PrettyTable

# table is an object using the PrettyTable class.
table = PrettyTable()

# Executing the table object's methods.
table.add_column("Pokemon Name", ["Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type", ["Grass", "Fire", "Water"])

# Changing the table object's attribute.
table.align = "l"

print(table)