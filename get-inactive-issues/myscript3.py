from github import Github
from github_token import GITHUB_TOKEN
from dateutil.parser import parse
import time
from datetime import date

g1 = Github(GITHUB_TOKEN)
#g1 = Github(user, password)
#add github `FUTHUB_TOKEN` (string)
start = time.clock()
thefile = open('test2.txt', 'w')
org = g1.get_organization('coala')
repo = org.get_repo('coala')
#Get issues for a repo
# GET /repos/:owner/:repo/issues
# :owner= coala
# :repo= coala, change it accordingly as per repo name

issues = repo.get_issues()
issues_number_list = []
issue1 = []
for myissue in issues:
    label = []
    for mylabel in myissue.labels:
        label.append(mylabel.name)
    if 'status/blocked' not in label:
        if myissue.state == 'open' and myissue.pull_request == None:
            issue1.append(myissue)

# Saving Issue object in list to decrease the time taken by code

for j in issue1:
    issue_no = j.number
    events = j.get_events()
    myevent = []
    data = []
    for i in events:
        myevent.append(str(i.event))
    for i in events:
        if i.commit_id is not None:
            data.append(str(i.created_at))
    for i, myevents in reversed(list(enumerate(myevent))):
        if myevents == 'unassigned':
            break
        elif myevents == 'assigned':
            a = events[i].created_at
            c  = (date.fromtimestamp(time.time()) -a.date()).days
            if c>=60: # for checking assigned duration

                mydata = list(reversed(data))
                if len(mydata)!=0:
                    commit1  = parse(mydata[0])
                    calculated_days = (date.fromtimestamp(time.time()) -commit1.date()).days
                    if calculated_days>=60: # for checking last commit update
                        issues_number_list.append(issue_no)
                else:
                    issues_number_list.append(issue_no)
            break

# Currenlty saving the list to `.txt` file
for item in issues_number_list:
	thefile.write("%s\n" % item)
print time.clock() - start
