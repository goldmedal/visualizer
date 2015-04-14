#!/usr/bin/env python

# Copyright (C) 2013 National Cheng Kung University, Taiwan
# All rights reserved.

# Configure wether to trace these feature
# Warning : Too many conte



log = open('log', 'r')
lines = log.readlines()
in_time = 0
out_time = 0
costs = [];

for line in lines :
	line = line.strip()
	inst, args = line.split(' ', 1)

	if inst == 'switch' :
		out_task, in_task, tick, tick_reload, out_minitick, in_minitick = args.split(' ')
		
		out_time = (float(tick) + (float(tick_reload) - float(out_minitick)) / float(tick_reload)) / 100 * 1000;
		in_time  = (float(tick) + (float(tick_reload) - float(in_minitick))  / float(tick_reload)) / 100 * 1000;
	
    
        cost = {}
        
        if in_time > out_time :
            cost['cost'] = in_time - out_time
            costs.append(cost)
             
             
log.close()

context_cost = open('cost', 'w')

i = 0

for cost in costs:
    context_cost.write("%d %f\n" % (i, cost['cost']))
    i = i + 1
    
context_cost.close()                	
        
