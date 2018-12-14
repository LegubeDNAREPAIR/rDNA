#Script : get_break_event.py
#But : For each line print total (RG,GR, RGR ...) and all events (like RG to RGR)
#Input : tab separator file wich contains on last column : G:G[7.10]R:R[5.16]-:_[38.08]
import re
import sys

number_line = 0
print("{:s}\t{:s}\t{:s}".format("line","total","number_of_event","type_of_event"))
total_total = total_event = 0  #Count total event form by the association of differents sub-units
with open(sys.argv[1]) as f:
	header = f.readline() #Extract header
	for line in f:
		info = line.strip("\n").split(";")[-1]

		my_sub_dict = ["".join(re.findall('.:(.)\[[0-9]*\.?[0-9]*\]',elmt)) for elmt in info.split("_")] #Extract elements for this line
		event = []
		for i in range(0,len(my_sub_dict)-1): #Parse my sub_dict for first element to last-1 
			if(my_sub_dict[i] == my_sub_dict[i+1]): #If actual element same that the next one
				continue
			else: #If not add as an mutation event
				event.append(my_sub_dict[i]+"|"+my_sub_dict[i+1])

		number_line +=1
		print("{:d}\t{:d}\t{:d}\t{:s}".format(number_line,len(my_sub_dict),len(event),(",").join(event)))
		total_total+=len(my_sub_dict)
		total_event+=len(event)
print("{:s}\t{:d}\t{:d}\t{:s}".format("TOTAL",total_total,total_event,""))

