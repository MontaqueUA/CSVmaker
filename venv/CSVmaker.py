import csv
import random
import string
import uuid


def make_string (row):
    result_string = ''
    last = len(row) - 1
    i = 0
    for num in row:
        if (i == last):
            result_string += str(num) + '\n'
        else:
            result_string += str(num) + ';'
        i += 1
    return result_string

with open('big_example.csv', 'w+') as csvfile:
    csvfile.write('ID;xcWt;SqS;ASQ;WQE;sss;qwe;aaaa;29a;daqr0;disq\n')
    # filewriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    # filewriter.writerow(['ID','xcWt', 'SqS', 'ASQ', 'WQE', 'sss', 'qwe', 'aaaa', '29a', 'daqr0','disq'])
    i = 0
    while i < 100000:
        j = 0
        newRow = []
        row_id = i
        #row_id = uuid.uuid4().hex
        #row_id = row_id.lower()[0:random.randint(2,8)]
        newRow.append(row_id)
        while j < 10:
            newRow.append(random.randint(0,999))
            j += 1
        i += 1
        string_row = make_string(newRow)
        csvfile.write(string_row)

