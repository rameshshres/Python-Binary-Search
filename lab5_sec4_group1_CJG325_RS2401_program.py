# Programmers: Cameron Gruich (cjg325) and Ramesh Shrestha (rs2401)

# import randint to generate random numbers for our list
#from random import randint

# import time to record function run times
from time import time

from math import log2

from random import randint

# Function: binary_search(listVar, numVar)
# Purpose: Performn a binary search on an ordered list for a desired value.
# Paramters: listVar (The list to look through), numVar (The number to look for)
#____________________________________________________________________________________
def binary_search(listVar, numVar):

    # Calculate list length
    listLength = len(listVar)

    # Set left index and right index to the start and end of the list, respectively.
    l_index = 0
    r_index = listLength - 1

    # While the indices have not crossed
    while l_index <= r_index:

        # Calculate the middle index and floor the result if it is not an integer
        mid_index = int((l_index + r_index)/2)

        # Have we found the value we want with the middle index? Good, return the middle index
        if listVar[mid_index] == numVar:

            choice = mid_index
            break
        # Is the value with the middle index bigger than the value we are looking for? Start searching at the left half of the list
        elif listVar[mid_index] > numVar:

            r_index = mid_index - 1
        # Is the value with the middle index less than the value we are looking for? Start searching at the right half of the list
        else:
 
            l_index = mid_index + 1

        # If the indices have crossed, return -1 because the value we want is not in the list.
        if l_index > r_index:

            choice = -1

    return choice
#______________________________________________________________________________________

# Function: binary_search_recursive(listVar, numVar, l_index, r_index)
# Purpose: Perform the binary search algorithm via recursion to find a value in a list
# Parameters: listVar (The list to search through), numVar (The number to look for), l_index (The left index position),
#             r_index (The right index position)
#____________________________________________________________________________
def binary_search_recursive(listVar, numVar, l_index, r_index):

    # Calculate the middle index
    mid_index = int((l_index + r_index) / 2)


    # Have the left and right indices crossed? Return -1
    if l_index > r_index:
        choice = -1
        
        #print("L", l_index, "  R", r_index, "  L/R crossed")
        #print("")
        
        return choice

    #print("L", l_index, listVar[l_index])
    #print("R", r_index, listVar[r_index])
    #print("M", mid_index, listVar[mid_index])
    #print("")



    # Have we found the value we are looking for with the middle index?
    # Return the middle index
    if listVar[mid_index] == numVar:
        choice = mid_index
        return choice

    # Is the value we found with the middle index greater than the value
    # we are looking for?
    elif listVar[mid_index] > numVar:
        # Set the right index to the left of the middle index
        r_index = mid_index - 1

        # Call the function again to only look to the left side of the list
        # and return the result
        recurse1 = binary_search_recursive(listVar, numVar, l_index, r_index)
        return recurse1

    # Is the value we found with the middle index less than the value we are
    # looking for?
    else:
        # Set the left index to the right of the middle index
        l_index = mid_index + 1

        # Call the function again to only look to the right side of the list
        # and return the result
        recurse2 = binary_search_recursive(listVar, numVar, l_index, r_index)
        return recurse2

#____________________________________________________________________________

# Define a sample list
testList = [11, 23, 34, 46, 58, 69, 73, 87, 90, 102, 115, 127, 133, 149, 154, 168, 179, 183, 195, 205]

# Starting position for right index. Indices start at 0, so we subtract one from
# the list length
start_right = len(testList) - 1

# Test case for the first vale in the list
print(testList)
print("")
print("looking for ", 11)
print("")
result1 = binary_search_recursive(testList, 11, 0, start_right)
print("Returned index: ", result1)
print("Expected index: ", 0)

if result1 == 0:
    print("test passed: YES")
else:
    print("test passed: NO")
print("")

# Test case for the last value in the list
print(testList)
print("")
print("looking for ", 205)
print("")
result2 = binary_search_recursive(testList, 205, 0, start_right)
print("Returned index: ", result2)
print("Expected index: ", 19)

if result2 == 19:
    print("test passed: YES")
else:
    print("test passed: NO")
print("")

# Test case for a value less than the first value in the list
print(testList)
print("")
print("looking for ", 2)
print("")
result3 = binary_search_recursive(testList, 2, 0, start_right)
print("Returned index: ", result3)
print("Expected index: ", -1)

if result3 == -1:
    print("test passed: YES")
else:
    print("test passed: NO")
print("")

# Test case for a value bigger than the last value in the list
print(testList)
print("")
print("looking for ", 300)
print("")
result4 = binary_search_recursive(testList, 300, 0, start_right)
print("Returned index: ", result4)
print("Expected index: ", -1)

if result4 == -1:
    print("test passed: YES")
else:
    print("test passed: NO")
print("")

# Test case for a value not in the list but, if it was, it would be somewhere in the middle.
print(testList)
print("")
print("looking for ", 106)
print("")
result5 = binary_search_recursive(testList, 106, 0, start_right)
print("Returned index: ", result5)
print("Expected index: ", -1)

if result5 == -1:
    print("test passed: YES")
else:
    print("test passed: NO")
print("")



# TIMING PORTION

# Make lists to hold our single run times and C values for our algorithms later.
timeRec = []
timeBin = []


CRec = []
CBin = []




# Define a list of sample sizes we want to test.
sampleSize = [256, 1024, 4096, 16384, 65536, 262144]

# Run the algorithms for a list of each sample size specified.
for value in sampleSize:
    unorderedList = []

    # Assign n random numbers to a list from 1 to n*n. Making the random integer range large helps prevent duplicates.
    for i in range(value):

        unorderedList.append(randint(1, 10000000))

    # We may have duplicates numbers next to each other in the list, which may give inaccurate results for the algorithm.
    # So, we need to eliminate duplicates.
    # We can do this by converting the list into a set using set(). Sets are unordered collections that only accept unique values.
    # So, using set() will automatically remove duplicates.
    orderedSet = set(unorderedList)

    # Convert the set with removed duplicates back into a list again
    myList = list(orderedSet)

    # Sort the list
    myList.sort()

    listLength = len(myList)

    # If we did remove m duplicates from the list of size n, then our new list size is n - m.
    # To give accurate results, let's re-add m terms randomly to the list and re-sort it.
    # i.e. A list of 2000 values with 2 duplicates removed is now 1998 values,
    # so lets add 2 values back to the list and re-sort it to make a new 2000 value'd list.
    while listLength < value:
        
        myList.append(randint(1, 10000000))

        myList.sort()

        listLength = len(myList)
     
    

    # Begin timing for recursive binary search
    timeStart1 = time()
    for rep1 in range(900000):
        recSearch = binary_search_recursive(myList, myList[value - 1], 0, (value - 1))
    # End timing
    timeEnd1 = time()

    timeDiff1 = timeEnd1 - timeStart1

    timeRec.append(format((timeDiff1/900000), ".3g"))

    # C = f(n) / n because sequential search is linear growth

    C1 = timeDiff1 / (900000 * log2(value))
    # Format for 3 significant values
    CRec.append(format(C1, ".3g"))



    # Being timing for binary search
    timeStart2 = time()
    for rep2 in range(900000):
        binSearch = binary_search(myList, myList[value - 1])
    # End timing
    timeEnd2 = time()

    timeDiff2 = timeEnd2 - timeStart2

    timeBin.append(format((timeDiff2/900000), ".3g"))



    # C = f(n)/log2(n) because the binary search is base 2 logarithmic growth (f(n) = C*log2(n))
    C2 = timeDiff2 / (900000*log2(value))
    # Format for 3 significant values
    CBin.append(format(C2, ".3g"))


    #___________________________________________#
# Print the results to the user.
print("\n\n")

# Binary Search Recursive Results
print("SAMPLE SIZES")
print(sampleSize)
print("\nRESULTS")
print("Binary Search Recursive Results")
print("Times")
print(timeRec)
print("Binary Search Recursive C Values")
print(CRec)

# Binary Search Results
print("\nBinary Search Results")
print("Times")
print(timeBin)
print("Binary Search C Values")
print(CBin)

