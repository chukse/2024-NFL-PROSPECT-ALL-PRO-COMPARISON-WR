from msilib.schema import Directory
import os
from time import time

# Using readlines()
#file1 = open('pass rush draft.txt', 'r')
file2 = open('wr all pro 2024 pff.txt', 'r')
#file3 = open('draft names.txt', 'r')
path_ = "C:/Users/chuke/Documents/WR compare/Data Folder/"
directory = os.fsencode(path_)

#go through folder and create of all files under 12 characters
file_list = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    filename = str(filename) 
    #print(filename)
        #print(file)
    if len(filename) != 'Null':
        test = path_ + filename
        stripped_line = test.rstrip()
        test = stripped_line
         
        file_list.append(test)
#print(file_list)

#Lines = file1.readlines()
average_allpro = file2.readlines()
#draft_names = file3.readlines() 
count = 0
combine_pffstats = []
allpro_combine = []
names = []


# Strips the newline character
#for line in Lines:
#    combine_pffstats.append(line)
for line2 in average_allpro:
    allpro_combine.append(line2)


average_for_allpro = []
Combine_line = []
player_comparison = []
average_for_allpro = allpro_combine[1].split('\t')
ideal_traits = []
for f in file_list:
    file1 = open(f, 'r')
    Lines = file1.readlines()
    for player in Lines:
        #print(player)
        Combine_line = player.rstrip('\n').split(',')
        #print(Combine_line)
        
        if (Combine_line[0] == 'player' ):
            continue
        
        else:
    


    
            if(Combine_line[8]== ''):
                contested_catch == float_avg_contested_catch
            else:
                contested_catch = float(Combine_line[8])
            #contested_catch = float(Combine_line[8])
    
    #print(true_prgrade)
            if(Combine_line[12]== ''):
                drop_rate == float_avg_dr
            else:
                drop_rate = float(Combine_line[12])
                
            #print(win_rate)
            #print(win_rate)
            if(Combine_line[17]== ''):
                grades_hands_drop == float_avg_ghd
            else:
                grades_hands_drop = float(Combine_line[17])
            
            grades_offense = float(Combine_line[19])
            
            if(Combine_line[21]== ''):
                grades_pass_route == float_avg_gpr
            else:
                grades_pass_route = float(Combine_line[21])
                
            if(Combine_line[28]== ''):
                pass_plays == float_avg_tps_pass_plays
            else:    
                pass_plays = float(Combine_line[28])
            
            targeted_qb_rating = float(Combine_line[35])
            
            if(Combine_line[43]== ''):
                yprr == float_avg_yprr
            else:    
                yprr = float(Combine_line[43])

            #average of all pro pff stats from college
            float_avg_contested_catch = float(average_for_allpro[8])
            #print(float_avg_prg)
            float_avg_dr = float(average_for_allpro[12])
            float_avg_ghd = float(average_for_allpro[17])   
            float_avg_go = float(average_for_allpro[19])
            float_avg_gpr = float(average_for_allpro[21])
            float_avg_tps_pass_plays = float(average_for_allpro[28])
            float_avg_tqbr = float(average_for_allpro[35])
            float_avg_yprr = float(average_for_allpro[43])
    
    
            
    

    

            if((float_avg_contested_catch -10 <= contested_catch <= float_avg_contested_catch +100)
                and ((float_avg_dr -10.00)  <= drop_rate <= (float_avg_dr+1.00))
                and ((float_avg_dr -2.00)  <= grades_hands_drop <= (float_avg_ghd + 300))
                and ((float_avg_go -7) <= grades_offense <= (float_avg_go + 300))
                and ((float_avg_gpr -15) <= grades_pass_route <= (float_avg_gpr + 300))
                and ((float_avg_tps_pass_plays -70) <= pass_plays <= (float_avg_tps_pass_plays + 300))
                and ((float_avg_tqbr -5) <= targeted_qb_rating <= (float_avg_tqbr + 300))
                and ((float_avg_yprr -3) <= yprr <= (float_avg_yprr + 300))
                and (Combine_line[2] == 'WR')
                #and (Combine_line[33] == '2023' or Combine_line[33] == '2022' )
                ):
                    player_comparison.append(player)
    
    


#for j in names:
    #for i in player_comparison:
        #named = i.split('\t')
        #if j == named[0]:
            #player_comparison.remove(i)


    #final_results = []
    #for i in player_comparison:
    #    named = i.rstrip('\n').split('\t')
    #    for n in names:
    #        na = n.rstrip('\n')
    #        if named[0] == na:
    #            final_results.append(i)

 



Lines = open('wr list.txt', 'r')
combinelist = Lines.readlines()
combine_list = []
player_profile = []   
for line in combinelist:
    combine_list.append(line)
pc = []
final_list = []
for player in combine_list:
    player_profile = player.rstrip('\n').split('\t')
    for player1 in player_comparison:
         pc = player1.rstrip('\n').split(',')
         if(pc[0]== player_profile[0]):
             final_list.append(player1)



      

with open('pff_stats2024.txt', 'w') as f:
    f.write('player	player_id	position	team_name	player_game_count	avg_depth_of_target	avoided_tackles	caught_percent	contested_catch_rate	contested_receptions	contested_targets	declined_penalties	drop_rate	drops	first_downs	franchise_id	fumbles	grades_hands_drop	grades_hands_fumble	grades_offense	grades_pass_block	grades_pass_route	inline_rate	inline_snaps	interceptions	longest	pass_block_rate	pass_blocks	pass_plays	penalties	receptions	route_rate	routes	slot_rate	slot_snaps	targeted_qb_rating	targets	touchdowns	wide_rate	wide_snaps	yards	yards_after_catch	yards_after_catch_per_reception	yards_per_reception	yprr\n')
    for w in final_list:
        f.write(w)
        f.write('\n')





        





