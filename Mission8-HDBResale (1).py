#Programming I

#########################
#      Mission 8        #
#   HDB Resale Prices   #   
#########################

#Background
#==========
#Tom is conducting some research into HDB resale prices as part of 
#his part-time work for a real estate agency.

#Write a program to find out the following:

#a) The 2017 average price for the 4-room flat type (in 2 decimal places)
#b) The number of transactions above the average resale prices in part (a)
#c) The town with the highest resale price for the 5-room flat type in 2017

#Return the result of the three parts in a list of 3 items
#(e.g., [34535.35,20,'Hougang']

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   four_room_average, above_average, town_highest

filename = "median-resale-prices-for-registered-applications-by-town-and-flat-type (1).csv"

#START CODING FROM HERE
#======================

#Create your function here
def ReadCSV(filename):
    file = open(filename)
    emp_list = []
    new_list = []
    final_list = []
    last_list = []
    B_list = []
    B1_list =[]
    B2_list = []
    B3_list =[]
    eve_list = []
    C_list = []
    C1_list = []
    final1_list = []

    #Part a
    for line in file:   
        if '4-room' in line:
            emp_list.append(line)
    
            
    for each in emp_list:
        index = each.find('\n')
        each1 = each.replace(each[index],'')
        new_list.append(each1)

    for line in new_list:
        if line[-1] != '-':
            final_list.append(line)
        
    for line in final_list:
        last_list.append(int(line[-6:]))
    
    four_room_average = sum(last_list)/len(last_list)
   


    #Part b
    file = open(filename)
    for line in file:
        B_list.append(line.replace('\n',''))
   
    B_list.remove(B_list[0])

    for line in B_list:
        if line[-1] != '-' and line[-2:] != 'na':
            B1_list.append(line)

    for l in B1_list:       
        if float(l[-6:]) > four_room_average:
            B2_list.append(l)
            
    for line in B2_list:
        if '4-room' in line:
            B3_list.append(line)
            
    above_average = (len(B3_list))
        

    #Part c
    file = open(filename)
    for line in file:
        if '5-room' in line:
            eve_list.append(line.replace('\n',''))
    
    for line in eve_list:
        if line[-1] != '-' and line[-2:] != 'na':
            C_list.append(line)
    
    
    total = 0
    for line in C_list:
        if int(line[-6:]) > total:
               total = int(line[-6:])
        
    for line in C_list:
        if int(line[-6:]) == total:
            C1_list.append(line)
   
    index1 = C1_list[0].find(',')
    
    index2 = C1_list[0].find('5')
    
    town_highest = C1_list[0][index1+1:(index2-1)]
    
    
    four_room_average = '{:.2f}'.format(four_room_average)

    print([four_room_average, above_average, town_highest])

    return [four_room_average, above_average, town_highest]

    
#Do not remove the next line
ReadCSV(filename)

#output [459567.74, 33, 'Toa Payoh']




