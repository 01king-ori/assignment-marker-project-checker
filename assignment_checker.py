# Define the question or the task
question = "Write a short paragraph about the causes of global warming."

# Define the list of expected keywords or phrases and their scores
keywords = [["greenhouse gases", 2], ["carbon dioxide", 1], ["deforestation", 1], ["fossil fuels", 1], ["climate change", 2]]

# Define the passing criteria
min_score = 5 # minimum score to pass
min_keywords = 3 # minimum number of keywords to pass

# Define the student's answer or solution
answer = "Global warming is the increase in the average temperature of the Earth's surface. "
# Apply the exact matching algorithm to the answer and compare it with the keywords
score = 0 # initialize the score
found = [] # initialize the list of found keywords
missing = [] # initialize the list of missing keywords
# Loop through each keyword and its score
for keyword, value in keywords:
  # Check if the keyword is in the answer
  if keyword in answer:
    # Add the score to the total score
    score += value
    # Add the keyword to the list of found keywords
    found.append(keyword)
  else:
    # Add the keyword to the list of missing keywords
    missing.append(keyword)

# Return the score and the feedback to the student
print(f"Your score is {score} out of {sum([value for keyword, value in keywords])}.")
print(f"You included {len(found)} keywords or phrases from the list: {', '.join(found)}.")
print(f"You missed {len(missing)} keywords or phrases: {', '.join(missing)}.")
# Check if the student passed or failed the assignment
if score >= min_score and len(found) >= min_keywords:
  print("You passed this assignment. Well done!")
else:
  print("You failed this assignment. Please review the topic and try again.")


