import csv



columns = []

#Values

print 'Which day is it? '
columns.append(raw_input().lower())

print 'How much time spent gaming?'
columns.append(raw_input().lower())

print 'How much time spent programing?'
columns.append(raw_input().lower())

print 'When did you go to bed?'
columns.append(raw_input().lower())

print 'When did you wake up?'
columns.append(raw_input().lower())

print 'How much did you study?'
columns.append(raw_input().lower())

print 'How much have you been reading other books?'
columns.append(raw_input().lower())

print 'How much did you exercise?'
columns.append(raw_input().lower())

print 'How much did you meditate?'
columns.append(raw_input().lower())

print 'For how long did you nap?'
columns.append(raw_input().lower())

print 'How much did you work?'
columns.append(raw_input().lower())

print 'For how long have you been on lectures today?'
columns.append(raw_input().lower())

with open('statLivet.csv', 'ab') as csvfile:
    CSVskriv = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    CSVskriv.writerow(columns)
