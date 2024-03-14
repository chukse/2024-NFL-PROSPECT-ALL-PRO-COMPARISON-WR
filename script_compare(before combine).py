from msilib.schema import Directory
import os
from time import time

# Using readlines()
file1 = open('wr combine results 2024.txt', 'r')
file2 = open('wr all pro.txt', 'r')

Lines = file1.readlines()
average_allpro = file2.readlines()
  
count = 0
Combine_results = []
allpro_combine = []


# Strips the newline character
for line in Lines:
    Combine_results.append(line)

for line2 in average_allpro:
    allpro_combine.append(line2)
    

average_for_allpro = []
Combine_line = []
player_comparison = []
ideal_traits = []
#Combine_line = Combine_results[2].split('\t')
#print(Combine_line)

average_for_allpro = allpro_combine[15].split('\t')
#print(average_for_allpro[1])
for player in Combine_results:
    Combine_line = player.rstrip('\n').split('\t')
    #print(Combine_line)
    
    if (Combine_line[0] == 'Name' ):
        continue
    
    #print(initial_height)
    initial_height = Combine_line[5].split('-')
    print(initial_height)
    #print(len(initial_height))
    feet = int(initial_height[0])
    inches = int(initial_height[1])
    height = float(feet*12 + inches)
    
    #height = round(int(Combine_line[4]), -1) 
    #print(height)
    if Combine_line[9] == '':
        arm_length = 35.13464286
    else:
        arm_length = float(Combine_line[9])
    
    #if Combine_line[14] == '--':
    #    broad_jump = 10.03
    #else:
        #r = Combine_line[13] %
    #    broad_jump = (float(Combine_line[14])) /100
    
    if Combine_line[7] == '':
        yd_dash = 4.48
    else:
        #r = Combine_line[7] %
        yd_dash = float(Combine_line[7]) 
    
    #if Combine_line[13] == '--':
    #    vert = 37.16666667
    #else:
        #r = Combine_line[13] %
    #    vert = float(Combine_line[13]) 
    if Combine_line[10] == '':
        hand = 9.384615385
        
    else:
        #r = Combine_line[7] %
        hand = float(Combine_line[10])
    
    
    
    int_avg1 = float(average_for_allpro[1])
    int_avg2 = float(average_for_allpro[2])
    float_avg3 = float(average_for_allpro[3])
    float_avg4 = float(average_for_allpro[4])
    float_avg5 = float(average_for_allpro[5])
    float_avg6 = float(average_for_allpro[6])
    float_avg7 = 10.03
    
    if Combine_line[10] == '':
        hand = 9.384615385
    weight = int(Combine_line[6])
    #print(int_avg1)
    #print(type(height))
    #print()
    #print(float_avg5)
    #print(yd_dash)
    if((int_avg1 -2 <= height <= int_avg1+4)
       and ((int_avg2 -10.00)  <= weight <= (int_avg2+10.00))
       and ((float_avg3 -2) <= arm_length <= (float_avg3 + 5))
       and ((float_avg4 - 1.0) <= hand <= (float_avg4+2.0))
       and ((float_avg5 - 1) <= yd_dash <= (float_avg5+.05))
       #and ((float_avg6 - 1.0) <= vert <= (float_avg6+10.0))
       #and ((float_avg7 - .5) <= broad_jump <= (float_avg7+1.0))
       ):
        player_comparison.append(player)
        
    

for i in player_comparison:
    print(i)

print(len(player_comparison))



with open('combine_measurement_matches.txt', 'w') as f:
    f.write('Name	School	Year	Position	Rank(by experts)	height	weight	40 yd dash	WINGSPAN	ARMLENGTH	HAND SIZE\n')
    for w in player_comparison:
        f.write(w)
        #f.write('\n')
