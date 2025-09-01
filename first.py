import suervy
table = suervy.Pregnancies()
table.ReadRecords()
print('Number of pregnancies',len(table.records))
table = suervy.Respondents()
table.ReadRecords()
print(table)