import xlsxwriter
import csv
import datetime

#Global
def write_in_worksheet(ws, column, text):
    ws.write(column, text)

columns = ['A1','B2','C2','D2', 'E2','F2','G2','H2','I2','J2','K2','L2','M2']

#Values
print 'Filename:'
name = raw_input().lower()

#Skapa excel
workbook = xlsxwriter.Workbook(name + '.xlsx')
ws1 = workbook.add_worksheet()

#title for colums
write_in_worksheet(ws1, 'A1', 'Day')
write_in_worksheet(ws1, 'B1', 'Gaming')
write_in_worksheet(ws1, 'C1', 'Programing')
write_in_worksheet(ws1, 'D1', 'Sleep')
write_in_worksheet(ws1, 'E1', 'Time Awake')
write_in_worksheet(ws1, 'F1', 'Studying')
write_in_worksheet(ws1, 'G1', 'Book')
write_in_worksheet(ws1, 'H1', 'Exercise')
write_in_worksheet(ws1, 'I1', 'Medidation')
write_in_worksheet(ws1, 'J1', 'Nap')
write_in_worksheet(ws1, 'K1', 'Work')
write_in_worksheet(ws1, 'L1', 'Lecture')

#Values to excel
#http://xlsxwriter.readthedocs.io/tutorial03.html

ma=[]

with open('statLIvet.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        ma.append(row)


#date_time = datetime.datetime.strptime('2013-01-23', '%Y-%m-%d')
#worksheet.write_datetime(0, 0, datetime, date_format)
#ws1.write(row, col + 1,kol2)  #text
ws1.set_column('A:A',20)
date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
row = 1
col = 0
for kol1,kol2,kol3,kol4,kol5,kol6,kol7,kol8,kol9,kol10,kol11,kol12 in (ma):
    ws1.write_datetime(row, col,datetime.datetime.strptime(kol1, '%Y-%m-%d'),date_format)
    ws1.write(row, col + 1,float(kol2) )
    ws1.write(row, col + 2,float(kol3))
    ws1.write(row, col + 3,float(kol4))
    ws1.write(row, col + 4,float(kol5))
    ws1.write(row, col + 5,float(kol6))
    ws1.write(row, col + 6,float(kol7))
    ws1.write(row, col + 7,float(kol8))
    ws1.write(row, col + 8,float(kol9))
    ws1.write(row, col + 9,float(kol10))
    ws1.write(row, col + 10,float(kol11))
    ws1.write(row, col + 11,float(kol12))
    row=row+1

workbook.close()



workbook.close()