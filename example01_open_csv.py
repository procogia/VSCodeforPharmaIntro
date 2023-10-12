import pandas


# Let's start with some Python list comprehensions
# Like lapply() in R, list comprehensions allow for fast processing 
# of items in a list without the need to use for loops
list_of_consecutive_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformed_num = [x ** 3 for x in list_of_consecutive_num]

# Adding * in this print statement prints without the brackets [] 
print(*transformed_num, '\n')


# This is the equivalent in for looping: 
empty_list = [] # Initialize empty list
for x in list_of_consecutive_num:
    x = x ** 3
    empty_list.append(x)

print(*empty_list, '\n')


###########################################
# Let's try a more complicated structure 
# Say you have a list of 'highest temp' recorded 
# Ints within the same list are temperature measurements taken on consecutive days
nestedLists = [[88,90,82,80,91,92,90,98,90,82,83,84], [101,88,85,85,86,80], [87,88,88,90,82,81]]
print(nestedLists, '\n')

# Which is the largest list in nestedLists? 
the_largest = max(nestedLists, key=len)
print(*the_largest, '\n')
# How many days were measured?
# print(len(the_largest))
# What the hottest temp on this particular record?
# print(max(the_largest))

# What are the hottest 3 consecutive days? 
# You can iterate via list comprehensions but I find for loops to make more sense
for little_list in nestedLists:
    
    hottest = max(little_list)
    ind = little_list.index(hottest)

    # If hottest temp happened right at the start
    if ind == 0:        
        print('The hottest consecutive temps are: ' + str(little_list[ind:ind+3]))
    elif ind == (len(little_list)+1): # if index is the last place        
        print('The hottest consecutive temps are: ' + str(little_list[(ind-2):ind]))
    # If index is not at last place but in middle    
    elif little_list[ind-2] > little_list[ind+1] and ind != (len(little_list)+1):        
        print('The hottest consecutive temps are: ' + str(little_list[(ind-2):(ind+1)]))
    elif little_list[ind+1] > little_list[ind-2] and ind != (len(little_list)+1):        
        print('The hottest consecutive temps are: ' + str(little_list[(ind-1):(ind+2)]))





###########################################


'''Since pandas is such an important and ubiquitous package 
our next exercise will cover doing simple tasks using pandas'''  

# Is pandas installed? 
# Get pandas version 
print(pandas.__version__)

# Open CSV file within same dir
test_frame = pandas.read_csv('./df_for_tutorial.csv')

# If your file's headers are not in the first row, 
# you can specify the number of rows you want to skip 
# test_frame = pandas.read_excel("./sample_df_preprocessing.xlsx", skiprows=range(0,4))

# Output to terminal to see your headers 
print(test_frame.head(), '\n')

# What are the column names?
print(test_frame.columns.tolist(), '\n')

# What are your unique values in the column "Compound_ID"?
print(test_frame['Compound_ID'].unique(), '\n')


# Does the Compound_ID 'COM01400' exist? 
print(test_frame[test_frame['Compound_ID'].str.contains('COM01400')], '\n')

# The above line returns an empty dataframe, the ID 'COM01400' does not exist in test_frame 

# What about this ID?
# This subsets the dataframe to just rows whose Compound_ID matches 'COMP09944'
print(test_frame[test_frame['Compound_ID'].str.contains('COMP09944')], '\n')

out_to_csv = test_frame[test_frame['Compound_ID'].str.contains('COMP09944')]

# Let's save a file with only entries whose Compound ID is 'COMP09944' 
out_to_csv.to_csv('target_subset.csv', index=False)