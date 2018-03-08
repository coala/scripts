# Get-inactive-issues
It find the issues that are assigned to somebody but that person hasn't shown
any activity in 2+ months(You can change it accordingly).

Support both Python2 and Python3

## Requirements
It uses
1. `PyGithub`.

...Install `PyGithub` using `pip install pygithub`
2. `python-dateutil`.

...Install `python-dateutil` using `pip install python-dateutil`

## How Does It work

 It uses a approach where it will first find that whether on issue someone is
 assigned or not, if yes this will check the duration, that when assignee was
 assigned, if duration was more than 60 days then it will check the date
 of last commit on issue and compare it with current date, if last commit
 was not updated more than 60 days it will return the issue number in
 text file.
