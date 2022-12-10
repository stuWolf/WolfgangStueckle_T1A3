>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''
>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines


Python File I/O

In this tutorial, you'll learn about Python file operations. More specifically, opening a file, reading from it, writing into it, closing it, and various file methods that you should be aware of.
Video: Reading and Writing Files in Python
Files

Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:

    Open a file
    Read or write (perform operation)
    Close the file

Opening Files in Python

Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

>>> f = open("test.txt")    # open file in current directory
>>> f = open("C:/Python38/README.txt")  # specifying full path

We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.

On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.
Mode
					Description
			
r
					Opens a file for reading. (default)
			
w
					Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
			
x
					Opens a file for exclusive creation. If the file already exists, the operation fails.
			
a
					Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
			
t
					Opens in text mode. (default)
			
b
					Opens in binary mode.
			
+
					Opens a file for updating (reading and writing)
			

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

Unlike other languages, the character a does not imply the number 97 until it is encoded using ASCII (or other equivalent encodings).

Moreover, the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.

So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

Hence, when working with files in text mode, it is highly recommended to specify the encoding type.

f = open("test.txt", mode='r', encoding='utf-8')

Closing Files in Python

When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.

Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.

f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()

This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

A safer way is to use a try...finally block.

try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop.

The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside the with statement is exited.

We don't need to explicitly call the close() method. It is done internally.

with open("test.txt", encoding = 'utf-8') as f:
   # perform file operations

Writing to Files in Python

In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.

We need to be careful with the w mode, as it will overwrite into the file if it already exists. Due to this, all the previous data are erased.

Writing a string or sequence of bytes (for binary files) is done using the write() method. This method returns the number of characters written to the file.

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

# This program will create a new file named test.txt in the current directory if it does not exist. If it does exist, it is overwritten.

# We must include the newline characters ourselves to distinguish the different lines.
# Reading Files in Python

# To read a file in Python, we must open the file in reading r mode.

# There are various methods available for this purpose. We can use the read(size) method to read in the size number of data. If the size parameter is not specified, it reads and returns up to the end of the file.

# We can read the text.txt file we wrote in the above section in the following way:

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''

# We can see that the read() method returns a newline as '\n'. Once the end of the file is reached, we get an empty string on further reading.

# We can change our current file cursor (position) using the seek() method. Similarly, the tell() method returns our current position (in number of bytes).

>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines

We can read a file line-by-line using a for loop. This is both efficient and fast.

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines

# In this program, the lines in the file itself include a newline character \n. So, we use the end parameter of the print() function to avoid two newlines when printing.

# Alternatively, we can use the readline() method to read individual lines of a file. This method reads a file till the newline, including the newline character.

f.readline()  # read each line by itself
'This is my first file\n'

f.readline()
'This file\n'

f.readline()
'contains three lines\n'

# 'write each line in a list'
f.readlines()
#output: 
['This is my first file\n', 'This file\n', 'contains three lines\n']

f.writelines(['writes', 'a', 'list', 'of' , 'lines'])
