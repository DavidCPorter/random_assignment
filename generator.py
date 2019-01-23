import pandas as pd
from master_dump import master
from random import shuffle


# def main():
dt = pd.read_csv('paper_reviews.csv', index_col=0).to_dict()
# students =
# print(dt)
# get a master list of the papers and add them as keys to a dict

# preprocess
# student

# for each student, look if they selected paper
papersToStudents = {el:[] for el in master.split(';')}

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

for student in studentsToPapers:
    print(student, '-->', studentsToPapers[student], '\n')





# print(studentsMap['Sidant Pani']['Architecture: Storage The Hadoop Distributed File System, Schvachko et al, MSST, 2010.'])


# if __name__ == '__main__':
#     main()
