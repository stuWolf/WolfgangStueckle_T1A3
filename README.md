## Investment calculator

Compound interest is a wonderfull thing, at least when you are in the plus! A lot of people don't even know what it is, so I decided to write this little program to make it visible. Also for a bit financial education for my children.
I am well aware that there are slready plenty of savings and mortgage calculators online, but first of all replicating things is a great way to learn. In addition to the calculators I have seen, my program also accepts negative numbers for Start Balance, Monthly deposit and yearly interest, that opens the way to many different new examples.
For example:
What happens to a -1000$ credit card balance at 25% when you leave it for 5 years?
Or what is the buying power of 10,000$ cash  at 4% inflation anfter 10 or 20 years? (set interest rate to -4%)
The program turned into a great tool for financial planning and education.


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
The program can also read a previously.csv file back and display the contents as graph.


# This is implemented in the following features:
1. Show input mask
get input data from user and check for plausibility, filter out 
invalid inputs

2. Calculate value of a future investment 
based on the input values:
initial Investment', Monthly Contribution, Annual interest rate, Compound frequency, Number of years of investment.



3. Show value of investment and monthly contribution in a table for each year of investment



4. Store value of investment and monthly contribution in a .CSV file for each year.




5. Plot chart with investment value and contribution over time"



6. Read from previous file and show data in a chart."





## R7: implementation plan and project management

[Project management](https://wolf-stueckle.atlassian.net/jira/software/projects/TA/boards/1/roadmap?shared=&atlOrigin=eyJpIjoiNDlmNmY2N2QzYTM3NDhlNTlmNmQwM2M5ZWI0OGZkYWYiLCJwIjoiaiJ9)
![Project plan screenshot](../WolfgangStueckle_T1A3/docs/terminal_application_2022-12-02_02.36pm.png)

# R8: Help documentation

## R8.1Installation

1. git clone git@github.com:stuWolf/WolfgangStueckleT1A3.git

2. cd WolfgangStueckleT1A3/src
run script ./calc_main.sh

as a back up I compiled a binary file with pyinstaller. it can be run stand alone with ./Calculator_main_bin or ./terminal_main_bin
## R8.2 Dependencies

## R8.3 System requirements
Runns on lynux/ PC

## R 8.4 How to use command line arguments












## Screenshot

![Project screenshot](../WolfgangStueckle_T1A3/docs/investment%20app.png)

## Tech stack

-python

-bash script

-git

-Markdown

## applications used
-pyinstaller to create single executable file, independant of python installation





## Target Audience

everybody who is interested in financial education