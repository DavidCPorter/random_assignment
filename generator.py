import pandas as pd
from master_dump import master
from random import shuffle


# def main():
dt = pd.read_csv('paper_reviews.csv', index_col=0).to_dict()

# for each student, look if they selected paper
papersToStudents = {el:[] for el in master.split(';')}


print('\n \n \n \n', "TOTAL NUMBER OF PAPERS ON THE LIST -> ", len(papersToStudents), '\n \n \n \n')

studentsToPreferredPapers = dict()
studentsToPapers = dict()
for i in dt['papers']:
    # populate new dict with students names -> papers(empty until assigned)
    studentsToPapers[i] = [];
    preferredPapers = dt['papers'][i]
    studentList = dict()
    for j in preferredPapers.split(";"):
        studentList[j] = True
    studentsToPreferredPapers[i] = studentList

randomPapers=list(papersToStudents.keys())
shuffle(randomPapers)

#give preference to students that submitted forms
for paper in randomPapers:
    for student in studentsToPreferredPapers:
    #iterate through the papers to see if the students chose, then add the student to the papersToStudents.
        try:
            if studentsToPreferredPapers[student][paper] == True:
                if len(papersToStudents[paper])<4 and len(studentsToPapers[student])<8:
                    papersToStudents[paper].append(student)
                    studentsToPapers[student].append(paper)
        except:
            pass

studentsLazy = []
for i in range(0,15):
    studentsLazy.append("student_"+str(i))
    studentsToPapers["student_"+str(i)]=[]


#students that did not submit will be assigned to the front of the reading list.
for paper in list(papersToStudents.keys()):
    for student in studentsLazy:
        if len(papersToStudents[paper])<4 and len(studentsToPapers[student])<8:
            papersToStudents[paper].append(student)
            studentsToPapers[student].append(paper)

print('\n\n', 'MAPPING OF STUDENTS -> PAPER:','\n\n\n')

for student in studentsToPapers:
    print(student, '\n-->', str(len(studentsToPapers[student]))+' assigned papers:', '\n', studentsToPapers[student],'\n')

print('\n\n', 'MAPPING OF PAPER -> STUDENTS:','\n\n')

for paper in papersToStudents:
    print(paper, '\n-->',str(len(papersToStudents[paper]))+' assigned students:', '\n', papersToStudents[paper],'\n')
