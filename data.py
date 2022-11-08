# Alec Rizzo
# Final Exam - Python
# Sorry this isn't the prettiest code.
# Anyways, hope you have a great day :)

# =====================================================================
def getAverage(num_list):
    sum = 0
    for x in range(len(num_list)):
        sum += int(num_list[x])
    return float(format((sum / len(num_list)), '.3f'))

 # I could have done this when reading the lines in main but
 # it deserved its own function
def getHistogram(list1, list2, list3):
    dict = {}
    for x in range(len(list1)):
         line_sum = int(list1[x]) + int(list2[x]) + int(list3[x])
         try:
             dict[line_sum] += 1
         except:
             dict[line_sum] = 1
    return dict
# =====================================================================

firsts = []
seconds = []
thirds = []

file = open('data.txt', 'r')
lines = file.readlines()
# Assign all the values to the appropriate lists from file
    # Since there are no double digit numbers this approach will work
for line in lines:
    line.strip()
    firsts.append(line[0])
    seconds.append(line[3])
    thirds.append(line[6])

histograms = getHistogram(firsts, seconds, thirds)

print(50*"=")
print("Average 1:", getAverage(firsts))
print("Average 2:", getAverage(seconds))
print("Average 3:", getAverage(thirds))
print(50*"=")
print("Histrogram of sums:")
temp = ()
for x in range(len(histograms)):
    temp = histograms.popitem()
    print(temp[0], "->", temp[1])

# =====================================================================
