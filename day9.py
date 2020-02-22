"""
@Question

You are given a list of data entries that represent entries and exits of groups of
 people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps. You can assume the building always starts off 
and ends up empty, i.e. with 0 people inside.

"""
def time_building_crowded(time_stamp_list):

    # stores the total number of people at a time stamp
    popln = [0]

    # get the population at each time stamp
    for i in range(1, len(time_stamp_list)):
        element = time_stamp_list[i] 
        if(element["type"] == "enter"):
            popln.append(popln[i-1] + element["count"])
        elif(element["type"] == "exit"):
            popln.append(popln[i-1] - element["count"])

    # get the time with the most/max number of people
    max_index = popln.index(max(popln))
    return (time_stamp_list[max_index], time_stamp_list[max_index+1])



# Populating time_stamp list 
population = [0, 3, -2, 4, -1, 3, 2, -5, -4, 0]
time_stamp_list = []
time_stamp =  1526579928
for i in population:
    time_stamp += 20
    if(i == 0):
        time_stamp_list.append({"timestamp": time_stamp, "count": 0, "type": "none"})
    elif( i > 0):
        time_stamp_list.append({"timestamp": time_stamp, "count": i, "type": "enter"})
    else:
        time_stamp_list.append({"timestamp": time_stamp, "count": -i, "type": "exit"})

#testing

assert time_building_crowded(time_stamp_list)[0]["timestamp"] == time_stamp_list[6]["timestamp"]

