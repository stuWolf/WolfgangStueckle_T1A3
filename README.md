## Investment calculator

Compound interest is a wonderful thing, at least when you are in the plus! A lot of people don't even know what it is, so I decided to write this little program to make it visible. Also for a bit financial education for my children.
I am well aware that there are already plenty of savings and mortgage calculators online, but first of all replicating things is a great way to learn. In addition to the calculators I have seen, my program also accepts negative numbers for Start Balance, Monthly deposit and yearly interest, that opens the way to many different new examples.
For example:
What happens to a -1000$ credit card balance at 25% when you leave it for 5 years?
Or what is the buying power of 10,000$ cash  at 4% inflation after 10 or 20 years? (set interest rate to -4%)
On the plus side if you give your child a $1000 at his birthday and put it into an investment funds at average return of 12%, how much would it be worth at 65? (Warren Buffets longterm return is actually 18%) Try it out. 
The program turned into a great tool for financial planning and education. I want to try to implement it as an app and integrate it as an example of my work in my profile page.


## R3 Attribution and Project Idea

[Compound interest calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator)

## R4 source control repository

git clone git@github.com:stuWolf/WolfgangStueckleT1A3.git

## R5 Code style guide

[code style guide](https://peps.python.org/pep-0008/)

## R6 List of features
The logic of the program is based on the compound interest formula: 
 A = P(1 + r/n)^(n*t) with P: start balance, r: interest rate, n: number of times interest is applied(compound frequency) t: number of years of investment and A the future value of the investment.
 For a one off start balance it is pritty straight forward, however it gets a little more interestig if the user starts making monthly deposits. basically each deposit needs to be run through the formula with t the time from the moment of deposit to the end of the period of investment. Each iteration needs to be added to the result.

The output would be how much you would have at the end of the Investment period and the chart. Optional this can be displayed in a table and stored in a .csv file.
The program can also read a previously generated .csv file back and display the contents as graph.


### This is implemented in the following features:
1. Show input mask
get input data from user and check for plausibility, filter out 
invalid inputs
I started implementing this program as a GUI based application because it is just so much more user friendly. However following the conversation on discord I realiced that this assignment is more about a terminal based application, so I wrote a terminal based user interface as well. I used the same set of functions for both versions, just the way I get the data from the user is different.

2. Calculate value of a future investment 
based on the input values:
initial Investment', Monthly Contribution, Annual interest rate, Compound frequency, Number of years of investment.

3. Show value of investment and monthly contribution in a table for each year of investment

4. Store value of investment and monthly contribution in a .CSV file for each year.

5. Plot chart with investment value and contribution over time.

6. Read from previous generated .csv file and show data in a chart.

Please see system overview for further details.
![Systemoverview](../WolfgangStueckle_T1A3/docs/System_overview.pdf)


## R7: implementation plan and project management

### R7.1 Implementation.pdf for each feature
Please see System overview and testplan
![Testplan](../WolfgangStueckle_T1A3/docs/Test_Plan.pdf)


![Systemoverview](../WolfgangStueckle_T1A3/docs/System_overview.pdf)
### R7.2 Prioritiy of implementation
Please see System overview , column priority

![Systemoverview](../WolfgangStueckle_T1A3/docs/System_overview.pdf)

### R7.3 Deadlines and duration
according to project management plan on Agile
[Project management](https://wolf-stueckle.atlassian.net/jira/software/projects/TA/boards/1/roadmap?shared=&atlOrigin=eyJpIjoiNDlmNmY2N2QzYTM3NDhlNTlmNmQwM2M5ZWI0OGZkYWYiLCJwIjoiaiJ9)
![Project plan screenshot](../WolfgangStueckle_T1A3/docs/terminal_application_2022-12-02_02.36pm.png)


## R8: Help documentation

### R8.1Installation

1. git clone git@github.com:stuWolf/WolfgangStueckleT1A3.git

2. I imlpemented 2 version of the program, one with GUI bansed on TKinter and one with terminal user interface.
change into WolfgangStueckleT1A3/src/gui_input
run script ./gui_input_main.sh  for GUI based user interface
or
change into WolfgangStueckleT1A3/src/term_input
run script ./term_input_main.sh  for terminal based user interface.

as a back up I compiled  binary files with pyinstaller and it can be run stand alone with ./gui_input_main_bin or ./term_input_main_bin. 

Both program files only run on the operation system the build was run which is Linux.

### R8.2 Dependencies
The programs have the following dependencies:
csv, datetime, mathplotlib.pyplot, numpy, mathplotlib.lines, os, sys, tkinter
Please also see system overview, column 'dependencies' for each function




### R8.3 System requirements
Runns on lynux/ PC

### R 8.4 How to use command line arguments
As in installation
