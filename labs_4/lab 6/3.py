def circuit_resistance(*resistances, connection='serial', conductivity=False):
    if connection == 'serial':
        total_resistance = sum(resistances)
    elif connection == 'parallel':
        total_resistance = 1 / sum(1 / r for r in resistances)
    else:
        total_resistance = sum(resistances)

    if conductivity:
        return round(1 / total_resistance, 4)
    else:
        return round(total_resistance, 4)


data = [10, 20, 30]
print(circuit_resistance(*data))
