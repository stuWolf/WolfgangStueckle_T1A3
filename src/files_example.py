# interact with files

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
def print_csv(P, m,  r, Compound_frequ, num_years):
    try:
        f = open("./src/test.csv",'w+',encoding = 'utf-8')
        f.write('Years, Accrued end of Year, Total Contributions\n')
    except Exception as e:
        print (e) 
    finally:
        pass


    for i in range(1,num_years+1, 1):
        capital = int(calculate_capital(P, m,  r, Compound_frequ, i))
 
   
        f.write(f'Year {i},{capital},{m*12*i} \n')
    

    f.close()
  
print_csv(0,100,18,'monthly' ,50)
# garbage collector  free mem as soon as program terminated

# book MVC Architecture