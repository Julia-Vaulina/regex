import re
import csv

new = []
new1 = []
phone = {}
title = {}
dict = {}
list_for_csv = []

with open("phonebook_raw.csv", encoding = 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  list = list(rows)

for i in list:
  pattern = r"(\+7|8)?(\s+)?\(?(\d{3})\)?-?(\s+)?(\d{3})-?(\d{2})-?(\d{2})(\s)?\(?(доб.\s\d{4})?\)?"
  result = re.sub(pattern, r"+7(\3)\5-\6-\7\8\9,", ','.join(i))
  new += [result]

for n in new:
  pattern1 = r"^(\w+)(,|\s)(\w+)(,|\s)(\w+)*(,{1,3})(\w+)*(,)?(position|\w*\s+.*[^\d][^,])?(,)"
  result1 = re.sub(pattern1, r"\1,\3,\5,\7,\9,", n)
  new1 += [result1.split(',')]

for nn in new1:
  for tt in nn:
      keys = tt.split(',')
  if (nn[0],nn[1]) not in phone:
      phone[nn[0],nn[1]] = nn[2:]
  else:
        for i in nn[2:]:
           if i not in phone[nn[0],nn[1]]:
             phone[nn[0],nn[1]] += [i]

for k,v in phone.items():
    list_for_csv += [[k[0],k[1]] + v]

with open("phonebook.csv", "w", encoding = 'utf-8') as f:
  datawriter = csv.writer(f)
  datawriter.writerows(list_for_csv)

