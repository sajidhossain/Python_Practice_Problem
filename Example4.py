records = []
list_name = []
for i in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
records.sort(key=lambda x: x[1])

new_records = []
first_score = records[0][1]
for j in range(len(records)):
    if records[j][1] != first_score:
        new_records.append(records[j])

second_score = new_records[0][1]
for k in range(len(records)):
    if records[k][1] == second_score:
        list_name.append(records[k][0])
for name in sorted(list_name, key=str.lower):
    print(name)
