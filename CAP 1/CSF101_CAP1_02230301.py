# Video References
# https://youtu.be/DE-ye0t0oxE?si=0X1al8H-aYClYcO6
# https://youtu.be/UldZOLylez4?si=JkBs6RTpJ3JnKc0u
# https://youtu.be/k_5Q_dHSMCw?si=E2RrAsfY4ICvCzmj
# https://youtu.be/R_wDA-PmGE4?si=z7hJeV4bkNyzCY2z
# https://youtu.be/Vca808JTbI8?si=ZKdgGQyRQ_f17nEU
# https://youtu.be/Uh2ebFW8OYM?si=5HERpgNu6tGKYjTa
# https://youtu.be/0EgSo7hsRWM?si=6MFdvv_tJKCv88Oq

# Article Reference 
# https://www.w3schools.com/python/python_scope.asp#gsc.tab=0
# https://www.w3schools.com/python/ref_func_zip.asp
# https://www.reddit.com/r/learnpython/comments/11yv1nu/how_to_make_a_table_without_additional_libraries/
# https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/
# https://stackoverflow.com/questions/63423004/multiple-binary-search-in-array-list

with open('02230301.txt','r') as file:
    data = file.readlines()
names_with_id = []
scores = []

def clean_data(x):
    global names_with_id
    global scores
    for line in x:
        
        line = line.strip()

        name_with_ID, score = line.split(',')
        
        names_with_id.append(name_with_ID)
        scores.append(int(score))
    return names_with_id , scores
names_with_id, scores = clean_data(data)
# print(names_with_id)

# Finding average
if scores:
    total_score = sum(scores)
    avg = total_score/len(scores)
else:
    avg = 0
# print(f"Average Score: {avg}")

# Applying bubble sort
def bubble_sort(comb):
    n = len(comb)
    for i in range(n):
        for j in range(0, n-i-1):
            #Comparing the scores
            if comb[j][1] > comb[j+1][1]:
                comb[j], comb[j+1] = comb[j+1], comb[j]
    return comb
# Combining two list
combined = list(zip(names_with_id,scores))
bubble_sorted_list = bubble_sort(combined)
# print(bubble_sorted_list)

#unzipping the file to  get the names and scores after bubble sort
bubble_sorted_names_with_id, bubble_sorted_scores = zip(*bubble_sorted_list)


# Applying insertion sort
def insertion_sort(comb):
    for i in range(1, len(comb)):
        element = comb[i]
        j = i-1
        while j>=0 and comb[j][1] > element[1]:
            comb[j+1] = comb[j]
            j -= 1
        comb[j+1] = element
    return comb
insertion_sorted_list = insertion_sort(combined)
# print(insertion_sorted_list)
#unzipping the file to  get the names and scores after insertion sort
insertion_sorted_names_with_id, insertion_sorted_scores = zip(*insertion_sorted_list)


#Lowest Scorer
lowest_scorer = bubble_sorted_list[0]
lowest_scorer_table = f"""
{'Lowest Score(s): '}
{'Lowest Score Table:'}
 {'Name':<20} | {'Score':<5} 
{'-'*30} 
 {lowest_scorer[0]:<20} | {lowest_scorer[1]:<5} 

"""
# print(lowest_scorer_table)

#Highest Scorer
highest_scorer = bubble_sorted_list[-1]
highest_scorer_table = f"""
{'Highest Score(s)'}
{'Highest Score Table:'}
 {'Name':<20} | {'Score':<5} 
{'-'*30} 
 {highest_scorer[0]:<20} | {highest_scorer[1]:<5} 

"""
# print(highest_scorer_table)

#Students scoring above average
above_average = []
for name, score in zip(bubble_sorted_names_with_id,bubble_sorted_scores):
    if score > avg:
        above_average.append((name, score))
# print (above_average)

#Students scoring below average
below_average = []
for name, score in zip(bubble_sorted_names_with_id,bubble_sorted_scores):
    if score < avg:
        below_average.append((name, score))
# print (below_average)


#Creating linear search algorithm 
def linear_search(to_search,target):
    result = []    
    for element in to_search:
        if element[1] == target:
            result.append(element)
        result_dict = {"Linear Search" : result}
    return result_dict

target_score = int(input("Enter the score to search for: "))
linear_search_results = linear_search(bubble_sorted_list,target_score)
# print(f"Linear searched results: {linear_search_results}")


#Creating binary search algorithm 
def binary_search_iterative(to_search,target):
    result = []
    left = 0
    right = len(to_search) - 1
    index_found = -1

    while left <= right:
        mid = left + (right - left) // 2
        if to_search[mid][1] == target:
            index_found = mid
            break
        elif to_search[mid][1] < target:
            left = mid + 1
        else:
            right = mid - 1
    # If there is no occurance of the targeted result, return dictionary with empty value
    if index_found == -1:
        return {"Binary Search(iterative)": result}
    # If the targeted value is present, replace index_found by index (searching if there is more then one targeted value)
    index = index_found
    while index >= 0 and to_search[index][1] == target:
        result.append(to_search[index])
        index -= 1
    index = index_found + 1
    while index < len(to_search) and to_search[index][1] == target:
        result.append(to_search[index])
        index += 1
    result_dict = {"Binary Search (iterative)": result}
    return result_dict

binary_search_results = binary_search_iterative(bubble_sorted_list,target_score)
# print(f"Binary searched results: {binary_search_results}")


# Writing output

with open('output.txt', 'w') as output_file:

    #Writing the average scores 
    output_file.write(f"Average Score: {avg}\n")


    #Writing the bubble sorted list
    output_file.write("\nBubble Sorted List:\n")
    output_file.write(f"{'Name':<20}| {'Score':<5}\n")
    output_file.write('-'*30 + '\n')
    for name , score in zip(bubble_sorted_names_with_id,bubble_sorted_scores):
        output_file.write(f"{name:<20} | {score:<5}\n")

    #Writing the insertion sorted list
    output_file.write("\nInsertion Sorted List:\n")
    output_file.write(f"{'Name':<20}| {'Score':<5}\n")
    output_file.write('-'*30 + '\n')
    for name , score in zip(insertion_sorted_names_with_id,insertion_sorted_scores):
        output_file.write(f"{name:<20} | {score:<5}\n")
    
    #Writing students scoring above average
    output_file.write("\nStudents Scoring Above Average\n")
    output_file.write("Above Average Students\n")
    output_file.write(f"{'Name':<20}| {'Score':<5}\n")
    output_file.write('-'*30 + '\n')
    for name , score in above_average:
        output_file.write(f"{name:<20} | {score:<5}\n")
    
    # Writing students scoring below average
    output_file.write("\nStudents Scoring Below Average\n")
    output_file.write("Below Average Students\n")
    output_file.write(f"{'Name':<20}| {'Score':<5}\n")
    output_file.write('-'*30 + '\n')
    for name, score in below_average:
        output_file.write(f"{name:<20} | {score:<5}\n")

    #Writing results found by implementing linear search algorithm
    output_file.write("\nSearch Results\n")
    for key, value in linear_search_results.items():
        output_file.write(f"{key} Result:\n")
        if value:
            for i in value:
                output_file.write(f"Name: {i[0]} | Score: {i[1]}\n")
        else:
            output_file.write("No result has been found.")
    
    #Writing results found by implementing Binary Search (iterative) algorithm
    for key, value in binary_search_results.items():
        output_file.write(f"\n{key} Result:\n")
        if value:
            for i in value:
                output_file.write(f"Name: {i[0]} | Score: {i[1]}\n")
        else:
            output_file.write("No result has been found.")    
print("Output file has been written")
    