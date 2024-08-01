from tabulate import tabulate

data = {
    "Nome": ["Alice", "Bob", "Charlie"],
    "Età": [24, 27, 22],
    "Città": ["Roma", "Milano", "Napoli"]
}

print(tabulate(data, headers="keys", tablefmt="grid"))