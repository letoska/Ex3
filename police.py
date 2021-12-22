with open ('1.txt', encoding="utf-8") as file1:
    account1 = len(file1.read())
with open('1.txt', encoding="utf-8") as file1:
    text1 = file1.read()
with open ('2.txt', encoding="utf-8") as file2:
    account2 = len(file2.read())
with open('2.txt', encoding="utf-8") as file2:
    text2 = file2.read()
with open ('3.txt', encoding="utf-8") as file3:
    account3 = len(file3.readlines())
with open('3.txt', encoding="utf-8") as file3:
    text3 = file3.read()
if account1 > account2 and account2 > account3:
    with open ('all.txt', 'w', encoding="utf-8") as all:
        all.write('1.txt\n')
        all.write(str(account1))
        all.write(text1)
        all.write('2.txt\n')
        all.write(str(account2))
        all.write(text2)
        all.write('3.txt\n')
        all.write(str(account3))
        all.write(text3)
if account2 > account1 and account1 > account3:
    with open ('all.txt', 'w', encoding="utf-8") as all:
        all.write('2.txt\n')
        all.write(str(account2))
        all.write(text2)
        all.write('1.txt\n')
        all.write(str(account1))
        all.write(text1)
        all.write('3.txt\n')
        all.write(str(account3))
        all.write(text3)
if account3 > account2 and account2 > account1:
    with open('all.txt', 'w', encoding="utf-8") as all:
        all.write('3.txt\n')
        all.write(str(account3))
        all.write(text3)
        all.write('2.txt\n')
        all.write(str(account2))
        all.write(text2)
        all.write('1.txt\n')
        all.write(str(account1))
        all.write(text1)