# stores subjects studies as variables
subjects = ['Math', 'Science', 'English']

# method to add a fourth subject you have studied to the end of the list.
subjects.append('History')

# method to return the index of one of the subjects in your list.
index = subjects.index('Science')

# Method used to Order the subjects alphabetically 
subjects.sort()

# method to make a copy of this list and store it in a different variable.
subjects_copy = subjects.copy()

# method to order this second list in reverse alphabetical order.
subjects_copy.sort(reverse=True)
print(subjects)