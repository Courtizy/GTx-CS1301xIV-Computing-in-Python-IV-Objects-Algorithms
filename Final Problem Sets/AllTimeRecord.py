#Let's try out a sort of data analysis-style problem. In
#this problem, you're going to have access to a data set
#covering Georgia Tech's all-time football history. The data
#will be a CSV file, meaning that each line will be a comma-
#separated list of values. Each line will describe one game.
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent
#
#If Points For is greater than Points Against, then Georgia
#Tech won the game. If Points For is less than Points Against,
#then Georgia Tech lost the game. If the two are equal, then
#the game was a tie.
#
#You can see a subsection of this dataset in season2016.csv
#in the top left, but the actual dataset you'll be accessing
#here will have 1237 games.
#
#Write a function called all_time_record. all_time_record
#should take as input a string representing an opposing team
#name. It should return a string representing the all-time
#record between Georgia Tech and that opponent, in the form
#Wins-Losses-Ties. For example, Georgia Tech has beaten
#Clemson 51 times, lost 28 times, and tied 2 times. So,
#all_time_record("Clemson") would return the string "51-28-2".
#
#We have gone ahead and started the function and opened the
#file for you. The first line of the file are headers:
#Date,Opponent,Location,Points For,Points Against. After that,
#every line is a game.


def all_time_record(opponent):
    #record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    record_file = open('temp_georgia_tech_football.csv', 'r')
    
    #Add some code here! Don't forget to close the file when 
    #you're done reading from it, before returning.
    lines = record_file.readlines()[1:]
    opponents_dict = {} #key is opponent team name, three more sub dicts with wins, losses, and ties!
    for line in lines:
        info_list = line.split(",")
        for info in info_list:
            if int(info_list[3]) > int(info_list[4].rstrip("\n")):
                if info_list[1] in opponents_dict.keys():
                    if "Wins Against" in opponents_dict[info_list[1]].keys():#Maybe .keys on outside square bracket?
                        opponents_dict[info_list[1]]["Wins Against"] += 1
                    else:
                        opponents_dict[info_list[1]]["Wins Against"] = 1
                else:
                    opponents_dict[info_list[1]] = {}
                    opponents_dict[info_list[1]]["Wins Against"] = 1
            elif int(info_list[4].rstrip("\n")) > int(info_list[3]):
                if info_list[1] in opponents_dict.keys():
                    if "Losses To" in opponents_dict[info_list[1]].keys():#here too, maybe
                        opponents_dict[info_list[1]]["Losses To"] += 1
                    else:
                        opponents_dict[info_list[1]]["Losses To"] = 1
                else:
                    opponents_dict[info_list[1]] = {}
                    opponents_dict[info_list[1]]["Losses To"] = 1
            elif int(info_list[3]) == int(info_list[4].rstrip("\n")):
                if info_list[1] in opponents_dict.keys():
                    if "Ties" in opponents_dict[info_list[1]].keys():#here too, maybe
                        opponents_dict[info_list[1]]["Ties"] += 1
                    else:
                        opponents_dict[info_list[1]]["Ties"] = 1
                else:
                    opponents_dict[info_list[1]] = {}
                    opponents_dict[info_list[1]]["Ties"] = 1
    for key in opponents_dict.keys():
        if "Ties" not in opponents_dict[key].keys():
            opponents_dict[key]["Ties"] = 0
        if "Wins Against" not in opponents_dict[key].keys():
            opponents_dict[key]["Wins Against"] = 0
        if "Losses To" not in opponents_dict[key].keys():
            opponents_dict[key]["Losses To"] = 0
    for key, value in opponents_dict.items():
        if key == opponent:
            return str(round(int(opponents_dict[key]["Wins Against"]) / 5)) + "-" + str(round(int(opponents_dict[key]["Losses To"]) / 5)) + "-" + str(round(int(opponents_dict[key]["Ties"]) / 5))
            #return int(opponents_dict[opponent]["Wins Against"]) / 5
    if opponent not in opponents_dict.keys():
        return "0-0-0"
    record_file.close()
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 51-28-2, 51-33-1, and 29-21-3, each on a separate
#line.
print(all_time_record("Clemson"))
print(all_time_record("Duke"))
print(all_time_record("North Carolina"))