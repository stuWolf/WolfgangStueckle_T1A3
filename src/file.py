# interact with files
from csv import reader
from formula import calculate_capital
# modes:
# rw
# w  write
# r  read
# f.write, starts fotm 0 possition
# f.append cursor last line
# f.close()

# try:
#     f = open('requirement.txt' , mode ='r+')  # if doesnt exist, open 
#     print(f.read(9)) # read line 9
#     f.write('i am here ')
#     f.newlines
#     f.write('i am here ')
#     f.close()
# except Exception as e:
#     print (e)
def store_csv(P, m,  r, Compound_frequ, num_years):
    try:
        f = open("investment_data.csv",'w+',encoding = 'utf-8')
        f.write('Years, Accrued end of Year, Total Contributions\n')
    except Exception as e:
        print (e) 
    finally:
        pass


    for i in range(1,num_years+1, 1):
        capital = calculate_capital(P, m,  r, Compound_frequ, i)
        f.write(f'Year {i},{capital},{round(m*12*i+P)} \n')

    f.close()
    print('investment_data.csv created in location of this program')




def file_read(file_name):




    accrued = []
    contribution = []

    with open(file_name, 'r') as csv_file:
         csv_reader = reader(csv_file)
         for row in csv_reader:
            accrued.append(row[1])
            contribution.append(row[2])
   
    accrued.pop(0)
    contribution.pop(0)

    accrued = [eval(i) for i in accrued]
    contribution = [eval(i) for i in contribution]
    return accrued, contribution


# file_name = './investment_data.csv'
# file_read(file_name)

# print(file_read(file_name))
# store_csv(10,100,18,'monthly' ,10)
