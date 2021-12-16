# PYTHON ALGORITHM FOR ALU GRADING SYSTEM
def gradingStudents(grades):
    # set the current gardes array to be empty
    finalGrades = []
    # loop through the array and check each grade
    for grade in grades:
        # check if a grade is below 38, it's a fail automotically
        if grade < 38:
            # append it to the array as it is
            finalGrades.append(grade)
        # if the difference between a grade and the next multiple of 5 is less than 3
        # round the grade up to the next multiple of 5
        elif grade % 5 > 2: 
            grade = (grade//5+1)*5
            # append the results to the list
            finalGrades.append(grade)
        # Any other grade that doesn't fit the criteria is automatically appended
        else:
            finalGrades.append(grade)
    # Return the list of grades
    return finalGrades
sample = [73, 67, 38, 33]
print(gradingStudents(sample))

