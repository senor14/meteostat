import csv
import datetime

# 날짜
current = datetime.datetime.now()
current = str(current)[0:10]
print(f'current={current}')

f_origin = open(f'E:\\Program\\Python\\Project\\csv\\{current}\\export.csv', 'r', encoding='utf-8')
f_modify = open(f'E:\\Program\\Python\\Project\\csv\\{current}\\output.csv', 'w', encoding='utf-8')
wr = csv.writer(f_modify)
rdr = csv.reader(f_origin)
for line in rdr:
  wr.writerow([line[0], line[1], line[3], line[4], line[9]])

f_origin.close()
f_modify.close()
