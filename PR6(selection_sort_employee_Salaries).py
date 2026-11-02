
salaries = [45000, 30000, 55000, 25000, 60000, 40000, 70000]

n = len(salaries)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if salaries[j] < salaries[min_index]:
            min_index = j

    salaries[i], salaries[min_index] = salaries[min_index], salaries[i]

print("Salaries in ascending order:")
print(salaries)

print("Top five highest salaries:")
print(salaries[-5:][::-1])
