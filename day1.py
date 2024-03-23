values = []


while True:
    try:
        value = input()
    except:
        break
    values.append(value)

elf_energy = [[]]
for value in values:
    if value == "":
        elf_energy.append([])
    else:
        elf_energy[-1].append(int(value))

energy_sums = []
for energies in elf_energy:
    energy_sums.append(sum(energies))

energy_sums.sort()

print(sum(energy_sums[-3:]))