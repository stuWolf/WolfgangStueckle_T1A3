## Investment calculator

My idea is to make an app that calculates the investment returns based on the compound interest formula and plots a chart that shows how much the investment grows over the years versus the contributions. The formula: A = P(1 + r/n)^(n*t) with P: start balance, r: interest rate, n: number of times interest applied(compound frequency) t: number of years and A the future value of the investment
 So start capital $1000, 18% annual return, $100 monthly contribu.tion and monthly compound for 1 year would be 1000(1 + 0.18/12)^12 + 100(1 + 0.18/12)^11 + 100(1 + 0.18/12)^10 + 100(1 + 0.18/12)^9 + . . . .+                100(1 + 0.18/12). Should be an easy for - loop.
So input would be: Initial investment, Monthly contribution, annual interest rate, compound frequency  (Monthly, annual, weekly). The output would be how much you would have at the end of the Investment period and the chart. Optional this can be displayed in a table and stored in a .csv file.




## Installation

 git clone git@github.com:stuWolf/WolfgangStueckleT1A3.git

cd WolfgangStueckleT1A3

## Project Idea

[Compound interest calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator)



## implementation plan anfd project management

[Project management](https://wolf-stueckle.atlassian.net/jira/software/projects/TA/boards/1/roadmap?shared=&atlOrigin=eyJpIjoiNDlmNmY2N2QzYTM3NDhlNTlmNmQwM2M5ZWI0OGZkYWYiLCJwIjoiaiJ9)

## Code style guide

[code style guide](https://peps.python.org/pep-0008/)

[Resource for logo maker](https://www.freelogodesign.org/)

## Images

[From Pixabay](https://pixabay.com/)
[From bing](https://bing.com/)

## Website link

[Wolfgang Stueckle portfolio](https://wolfstueckleportfolio.netlify.app/)

## Screenshot

![Website home page](./docs/Screenshot3.png)

## Tech stack

-python

-bash script

-git

-Markdown

## applications used
-pyinstaller to create single executable file, independant of python



## Sitemap and wireframes
!["Figma view"](./docs/Wire%20frame%20I%20phone.png)


!["Browser view"](./docs/Screenshot3.png)

## Target Audience

everybody who is interested in financial education