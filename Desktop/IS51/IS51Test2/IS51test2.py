"""
On a final exam, the program is attempting to show student grades.
The grades of 24 students are stored in a text file called "final.txt".
The number of grades, the average grade, and the grades that are above the average must all be calculated. 
Then print out the output, "Number of grades", "Average grade", "Percentage of grades above average". 
"""

"""
Get grade from Final.txt and display the number of grades in the text file
Compute average grade by average = sum of grades / number of grades in the list
Determine percentages of grades above average
if grade > average then add into the percentage of grades above average
"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grade above average: {0:.2f}%".format(100 * num / len(grades)))