import re
import sys



number_line = 0
print("{:s}\t{:s}\t{:s}".format("line","total","number_of_event","type_of_event"))
total_total = total_event = 0
with open(sys.argv[1]) as f:
	header = f.readline()
	for line in f:
		info = line.strip("\n").split(";")[-1]

		my_sub_dict = ["".join(re.findall('.:(.)\[[0-9]*\.?[0-9]*\]',elmt)) for elmt in info.split("_")]
		event = []
		for i in range(0,len(my_sub_dict)-1):
			if(my_sub_dict[i] == my_sub_dict[i+1]):
				continue
			else:
				event.append(my_sub_dict[i]+"|"+my_sub_dict[i+1])

		number_line +=1
		print("{:d}\t{:d}\t{:d}\t{:s}".format(number_line,len(my_sub_dict),len(event),(",").join(event)))
		total_total+=len(my_sub_dict)
		total_event+=len(event)
print("{:s}\t{:d}\t{:d}\t{:s}".format("TOTAL",total_total,total_event,""))
