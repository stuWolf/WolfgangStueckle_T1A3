# interact with files


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

try:

    f = open("./Lesson 8/test.csv",'w+',encoding = 'utf-8')
    f.write("my first file \n")
    f.write('i am here ')
    f.write("This file\n\n")
    f.write("contains three lines\n")
except Exception as e:
    print (e)
finally:
    f.close()
  

# garbage collector  free mem as soon as program terminated

# book MVC Architecture