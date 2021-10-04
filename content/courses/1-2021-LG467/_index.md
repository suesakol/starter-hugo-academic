---
title: LG 467 Computers in Linguistics
type: page
summary: 'This undergraduate-level course introduces students to key concepts in computational linguistics/natural language processing. The course covers basic text processing with Python.'
date: '2021-07-30'
lastmod: '2021-10-02'

# Optional header image (relative to `assets/media/` folder).
header:
  caption: ""
  image: ""
---


## Course information

**Instructor**:       Sakol Suethanapornkul       <br>
**Email**:              `suesakol@staff.tu.ac.th` <br>
**Office Hours**:  W & TH from 1 p.m. to 4 p.m.   <br>
**Room**:             Online via Zoom             <br>
**Time**:               W 9:30-12:30              <br>
**Credits**:           3/48 hours

-----


*The course syllabus provides a general plan for the course; some modifications may be necessary in response to students’ needs and classroom interaction.*

&nbsp;



## Course Description
แนวคิดพื้นฐานทั่วไปทางภาษาศาสตร์คอมพิวเตอร์ และความสำคัญของการใช้คลังข้อมูลทางภาษา ฝึกทักษะเบื้องต้นการใช้คอมพิวเตอร์ในการเก็บและวิเคราะห์ข้อมูลทางภาษาและภาษาศาสตร์

The course introduces students to computational linguistics (CL)/natural language processing (NLP), with a particular emphasis on concepts, models, and algorithms that aid the analysis of natural languages. The course aims to blend theoretical discussions with hands-on training in text processing using Python. We will begin by learning how computers encode written and spoken language. We will then examine the applications of CL/NLP methods to a range of linguistic phenomena. The topics we will cover include tokenization, part-of-speech tagging, parsing, corpus exploration, and others. Hands-on components of the course include learning basic programming in Python.

&nbsp;



## Course Objectives
By the end of this course, you should be able to do the following:
1. demonstrate a basic understanding of how computers work with natural languages and support language-related tasks;
2. recognize and describe key concepts in CL/NLP behind current real-world applications; and
3. write programs in Python to manipulate and analyze language data

&nbsp;


## Classroom-based Expectations
1. **Collaboration is encouraged.** Students are strongly encouraged to collaborate on their assignments. However, each student must submit their own original work (both homework assignments and programming exercises). Additionally, students who have worked with their friends must acknowledge their collaboration in their submission, unless stated otherwise in the assignment. 

2. **Timely submission of assignments is expected.** All work must be submitted before the due date as stated on the syllabus. I have the right to refuse acceptance of any late assignment. Please communicate with me early if you anticipate having trouble completing any assignment in a timely manner.

3. **Plagiarism is not tolerated.** Plagiarizing other people's work in an assignment results in an automatic zero for that assignment.

4. **Completion of weekly readings before class is critical.** You are expected to complete readings before class and come to class prepared to ask questions and/or participate in class discussion.

&nbsp;



## Prerequisites
Successful completion of LG 211 Introduction to Linguistics (with C or above) is required. You do not need to have any programming experience to complete this course. You are expected, however, to bring your own laptop to class and ensure that it runs either Windows 10 or Mac OS 10.15 (Catalina) or above. Tablets or smartphones are generally not recommended. Talk to me if you need help with the university's laptop assistance program. :smiling_face_with_three_hearts:

&nbsp;



## Textbooks
1. Dickinson, M. et al. (2013). *Language and computers*. West Sussex, UK: Wiley-Blackwell. [L & C for short]
2. Jurafsky, D., & Martin, J. H. (2020). *Speech and language processing* ([3rd ed. online draft](https://web.stanford.edu/~jurafsky/slp3/)). [J & M for short]
3. Bird, S. et al. *Natural language processing with Python* ([online edition for Python 3](https://www.nltk.org/book/)). [NLTK for short]

&nbsp;



## Course organization
In most cases, each class meeting will have lecture and practice components. During the first half of each class, we will cover topics presented in textbooks (L & C or J & M). As for the other half, you will receive hands-on training with Python and [Natural Language Toolkit (NLTK)](http://www.nltk.org).

Course management is done through **this course website** and **MS Teams**. You can obtain course materials (syllabus, slides, assignments, etc.) from this website. Assignment submissions, class announcements, and grades will be handled through MS Teams.

&nbsp;



## Assignments and Grading

### Grading scale:
In this course, I assign grades based on how well students perform. The grading scheme outlines key letter grades:

|   |Grades       |   |  Points              |  |  |Grades       |  |  Points              | 
|---|:------------|---|:---------------------|--|--|:------------|--|:---------------------|
|   | A           |   |  85-100%             |  |  | C           |  |  65-69.99            |
|   | B+          |   |  80-84.99            |  |  | D+          |  |  60-64.99            |
|   | B           |   |  75-79.99            |  |  | D           |  |  55-59.99            |
|   | C+          |   |  70-74.99            |  |  | F           |  |  0-54.99             |


### Grade breakdown:

|  Requirements              | Percent      | Points                       | Note    |
|:---------------------------|:------------:|:-----------------------------|:-------------------------------------------|
| Homework assignments       | 50%          | 10 points each, 6 in total   |                                            |
| Programming exercises      | 40%          | 10 points each, 5-6 planned  | Exercise with lowest mark dropped[^1]      |
| Participation              | 5%           |                              |                                            |
| Attendance                 | 5%           |                              | Up to one unexcused absence allowed        |


### Overview:

- Homework (i.e., assignments and exercises) is assigned on an approximately weekly basis. Typically, it will be **distributed on Wednesday after class** and due **Saturday night of the same week**. Extensions **may** be granted only in special circumstances (e.g., family or medical emergencies). Please communicate these to me in advance whenever possible.

- Both assignments and exercises will be weighted equally in their respective categories. The assignment with the lowest mark will be dropped.

- To receive full credit for attendance and participation, you are expected to come to class on time and engage meaningfully with the class content, including participating in class discussion. 

- You are allowed no more than one unexcused absence without affecting your course grade. This does not include excused absences due to illness or religious observances.


&nbsp;



## Class Schedule[^2]

|Weeks |  Dates       | Topics                               | Readings    | Assignments                      |
|----- |:------------:|:-------------------------------------|-------------|-------------------------------   |
|  1   | 08/11/21     | Course introduction <br>                                                                                                    [{{% staticref "467LC_2021/Slides/LG467.pdf" %}}Introduction{{% /staticref %}}]                                                                                      |             | {{% staticref "467LC_2021/HW/HW1.pdf"%}}                                                                                      HW 1{{% /staticref %}}: Key terms|
|  2   | 08/18/21     | Encoding language & Python installation <br>                                                                                [{{% staticref "467LC_2021/Slides/LG467-2.pdf" %}}Encoding{{% /staticref %}}, {{% staticref                                 "467LC_2021/Slides/LG467-Py1.pdf" %}}Installation{{% /staticref %}}]                                                                                                   | L & C Ch. 1 <br> (Sec. 1.1 and 1.3)                                                                                                       | {{% staticref "467LC_2021/HW/HW2.pdf"%}}                                                                                    HW 2{{% /staticref %}}: Unicode    |
|  3   | 08/25/21     | Python basics: Strings and string methods <br>                                                                              [{{% staticref "467LC_2021/Slides/LG467-Py2.pdf" %}}The Basics{{% /staticref %}}] <br>                                        [Python code: {{% staticref "467LC_2021/Scripts/CL3.py" %}}CL3.py{{% /staticref %}}]                                                                                  | [NLTK Ch. 1](https://www.nltk.org/book/ch01.html)                                                                                        | {{% staticref "467LC_2021/HW/Exercise1.py"                                                                                 %}}Exercise 1{{% /staticref %}}: Strings                                                                                                                          |
|  4   | 09/01/21     | Text normalization <br>                                                                                                     [{{% staticref "467LC_2021/Slides/LG467-3.pdf" %}}Tokenization{{% /staticref %}},                                             {{% staticref "467LC_2021/Slides/LG467-Py3.pdf" %}}Control & Conditions{{% /staticref %}}] <br>                               [Python code: {{% staticref "467LC_2021/Scripts/CL4.py" %}}CL4.py{{% /staticref %}}]                                                                                  | L & C Ch. 3 <br> (Sec. 3.3 and 3.4)                                                                                                     | {{% staticref "467LC_2021/HW/Exercise2.py"                                                                                 %}}Exercise 2{{% /staticref %}}: Palindrome                                                                                                                        |
|  5   | 09/08/21     | Text normalization (cont.) <br>                                                                                             [{{% staticref "467LC_2021/Slides/LG467-4.pdf" %}}Tokenization (2) & etc.{{% /staticref %}}] <br>                             [Python code: {{% staticref "467LC_2021/Scripts/CL5.py" %}}CL5.py{{% /staticref %}}]                                                                                  | [NLTK Ch. 3](http://www.nltk.org/book/ch03.html) <br>                                                                       (Sec 3.1, 3.2, 3.6)                                                                                                                       | {{% staticref "467LC_2021/HW/HW3.pdf"%}}                                                                                    HW 3{{% /staticref %}}: Text normalization                                                                                                                        |
|  6   | 09/15/21  | Regular expressions (Regex) & FSA <br>                                                                                        [{{% staticref "467LC_2021/Slides/LG467-5.pdf" %}}Regex{{% /staticref %}}] <br>                                               [Python code: {{% staticref "467LC_2021/Scripts/CL6.py" %}}CL6.py{{% /staticref %}}]                                                                                   | J & M Ch. 2 <br>                                                                                                              (Sec. 2.1) <br>                                                                                                               L & C Ch. 4 <br>                                                                                                              (Sec. 4.4) | Exercise 3: RE                   |
|  7   | 09/22/21  | Regex (cont.) & Corpora <br>                                                                                                 [{{% staticref "467LC_2021/Slides/LG467-6.pdf" %}}Regex (2){{% /staticref %}}, {{% staticref                                  "467LC_2021/Slides/LG467-7.pdf" %}}Corpus (1){{% /staticref %}}]  <br>                                                        [Python code: {{% staticref "467LC_2021/Scripts/CL7.py" %}}CL7.py{{% /staticref %}}]                                                                                     |          | No assignment                     |
|  8   | 09/29/21  | Mid-term examination week                 |          |                                   |
|  9   | 10/06/21  | Corpus exploration <br>                                                                                                      [{{% staticref "467LC_2021/Slides/LG467-8.pdf" %}}Corpus (2){{% /staticref %}}] <br>                                          [Python code: {{% staticref "467LC_2021/Scripts/CL8.py" %}}CL8.py{{% /staticref %}}]                                                                                    |           | {{% staticref "467LC_2021/HW/HW4.pdf" %}} HW 4{{%                                                                             /staticref %}}: Frequency counts <br> ({{%                                                                                    staticref "467LC_2021/HW/HW4.zip" %}}HW4.zip{{%                                                                               /staticref%}})                    |
|  10  | 10/13/21  | Holiday: King Bhumibol Memorial Day   |             |                                   |
|  11  | 10/20/21  | Part-of-speech tagging                |             |                                   |
|  12  | 10/27/21  | Part-of-speech tagging                |             |                                   |
|  13  | 11/3/21   | Syntactic parsing                     |             |                                   |
|  14  | 11/10/21  | Mental Health Week <br>                                                                                                     Relax, meditate, and catch up on your sleep! | :heart: |   No assignment                |
|  15  | 11/17/21  | Syntactic parsing                    |             |                                 |
|  16  | 11/24/21  | Biases in NLP & looking ahead        |             |                                 |

&nbsp;



## Resources

- {{% staticref "467LC_2021/Scripts/News.txt"%}}Business news report (CNBC){{% /staticref %}}
- {{% staticref "467LC_2021/Scripts/Song.txt"%}}Children's song: If you're happy and you know it{{% /staticref %}}

&nbsp;



## Footnotes

[^1]: This depends on the total number of exercises. I will communicate with you as soon as possible if there is any change to the calculation of the grading.
[^2]: Last day of the semester falls on November 27, 2021.
