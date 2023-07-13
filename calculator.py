
v = []
h = False
flag = True
while True:
    x = input()
    if x == '':
        break
    l = x.split()
    if len(l) != 3:
        flag = False
    if not l[0][0].isalpha(): 
        print("improper course no")
    if not l[0][-1].isdigit():
        print("improper course no")
    if l[1] not in ["1", "2", "4"]:
        print("incorrect credit")
    if l[2] not in ["A+", "A", "A-", "B", "B-", "C", "C-", "D", "F"]:
        print("incorrect grade")
    else:
        s = l[0]
        for chr in s:
            if not (64 < ord(chr) < 91 or 96 < ord(chr) < 123 or 47 < ord(chr) < 58):
                flag = False
                break
        if flag == False:
            break
        if l[1] not in ['1', '2', '4']:
            flag = False
        if l[2] not in ['A+', 'A', 'A-', 'B', 'B-', 'C', 'C-', 'D', 'F']:
            flag = False
        if flag == True:
            v.append((l[0], int(l[1]), l[2]))
    if flag == False:
        print('Invalid input')
        h = True

if len(v)>0:
    v.sort()
    for course in v:
        print(f'{course[0]}: {course[2]}')
    grades = {'A+': 10, 'A': 10, 'A-': 9, 'B': 8, 'B-': 7, 'C': 6, 'C-': 5, 'D': 4, 'F': 2}
    total_credits = 0
    points = 0

    for course in v:
        total_credits += course[1]
        points += course[1] * grades[course[2]]
    sgpa = points / total_credits
    print(f'SGPA: {sgpa:.2f}')
