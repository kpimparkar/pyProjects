import requests
from bs4 import BeautifulSoup
import sys

link='https://www.sice.indiana.edu/graduate/degrees/data-science/courses/index.html'
try:
    html_data=requests.get(link).text
except Exception as e:
    print("Could not fetch the webpage: {}".format(e))
    sys.exit(e)

print("Webpage accessed successfully.")
soup_object=BeautifulSoup(html_data,"lxml")
tab1=soup_object.find('div',id='tabs-1')

#dept For loop will be required
####dept = tab1.find('div',class_="department")
for dept in tab1.find_all('div',class_="department"):
    dept_name = tab1.h3.text
    print(dept_name)

    #course for loop reqd
    #####course = tab1.section.p
    for course in tab1.find_all('section'):
        #print(course)
        course_name = course.strong.text
        print(course_name)
        course_data=str(course).split('<br/>')
        for i in course_data:
                if 'Class' in i:
                        class_name=i.strip().replace('<strong>','').replace('</strong>','')
                        print(class_name)
                if 'Section:' in i:
                        sec_name=i.strip().replace('<strong>','').replace('</strong>','')
                        print(sec_name)
                if 'Syllabus:' in i:
                        syllabus=i.strip().replace('<strong>','').replace('</strong>','')
                        #print(syllabus, type(syllabus))
                        if 'href' in i:
                                soupsyll = BeautifulSoup(syllabus,"lxml")
                                syllabus=soupsyll.a['href']
                                print("Syllabus: ", syllabus)
                if 'Instructor:' in i:
                        prof=i.strip().replace('<strong>','').replace('</strong>','')
                        #print(prof)
                        if 'href' in i:
                                soupprof = BeautifulSoup(prof,"lxml")
                                prof = soupprof.a.text
                                print("Instructor: ", prof)
                if 'Synopsis:' in i:
                        synopsis=i.replace('</p>','').strip().replace('<strong>','').replace('</strong>','')
                        print(synopsis)
        print("====================")

