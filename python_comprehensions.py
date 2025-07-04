#------------------------LIST COMPREHENSIONS-----------------------

#1. Use a list comprehension to filter all the scores above 60 and store them in a new list called passed.
scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]

# code
passed = [x for x in scores if x > 60]
print(passed)

#2. Use another list comprehension to convert all scores into "Pass" or "Fail" using a threshold of 50.
new_scores = ['pass' if score >= 50 else 'fail' for score in scores] 
    #the conditional logic is placed at the beginning of the list comprehension when changing list values.
print(new_scores)

#------------------------DICTIONARY COMPREHENSIONS-----------------------

#3. Create a dictionary using comprehension that pairs each student with their mark.
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]

#code
students_marks = {k: v for k , v in zip(students, marks)}
print(students_marks)

#4. Create a second dictionary that stores only students who scored more than 70.
students_marks = {k: v for k, v in zip(students, marks) if v > 70}
print(students_marks)

#5. Create a third dictionary that maps each student to "Pass" or "Fail" (threshold: 50).
students_marks = {k: ('pass' if v >= 50 else 'fail') for k, v in zip(students, marks)}
print(students_marks)

#6. Write a dictionary comprehension that maps each word to its length.
sentence = "Data science is fun and insightful"

#code
word_dict = {word: len(word) for word in sentence.split()}
    #sentence.split() - splits the sentence string into a list of words using spaces as delimeters;
    #dictionary comprehension - iterates each word in the list and generates key-value pairs made of the word itself and it's length respectively.
print(word_dict)


