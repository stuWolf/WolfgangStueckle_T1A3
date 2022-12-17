# interact with files
from csv import reader
from formula import calculate_capital
from datetime import date


# modes:
# rw
# w  write
# r  read
# f.write, starts fotm 0 possition
# f.append cursor last line
# f.close()


def store_csv(P, m,  r, Compound_frequ, num_years):
    today = str(date.today())
    filtered_date= ''.join((filter(lambda x: x not in ['-'], today)))
    try:
        f = open(f'./invest_data{filtered_date[2:8]}.csv','w+',encoding = 'utf-8')
        #f = open("data.csv",'w+',encoding = 'utf-8')
        f.write('Years, Accrued end of Year, Total Contributions\n')
    except Exception as e:
        print (e) 
    finally:
        pass


    for i in range(1,num_years+1, 1):
        capital = calculate_capital(P, m,  r, Compound_frequ, i)
        f.write(f'Year {i},{capital},{round(m*12*i+P)} \n')

    f.close()
    print(f'invest_data{filtered_date[2:8]}.csv created in the path of your terminal')
 



def file_read(file_name):




    accrued = []
    contribution = []

    with open(file_name, 'r') as csv_file:
         csv_reader = reader(csv_file)
         # the csv.reader function returns a list of lists, with each row in a file as a seperate list
         # read the 2nd and the third element of each list and write it in a new list
         # the result is a list for each column that can be processed by the plot function
         for row in csv_reader:
            accrued.append(row[1])
            contribution.append(row[2])
   # loose the column name
    accrued.pop(0)
    contribution.pop(0)


# convert the list of strings to list of integer
    accrued = [eval(i) for i in accrued]
    contribution = [eval(i) for i in contribution]

    # print(accrued)
    # print(contribution)

    return accrued, contribution

# test for read file
# file_name = 'invest_data221218.csv'
# # file_read(file_name)
# print(file_read(file_name))

# test for create and store_csv
# store_csv(10,100,18,'monthly' ,10)
