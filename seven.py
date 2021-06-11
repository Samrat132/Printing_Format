# You live 4 miles from university.
# The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
# How long will the bus journey take?
# Alternatively, you could run to university.
# You jog the first mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again.
# Will this be quicker or slower than the bus?

dist_to_uni = 4

#for bus
bus_speed =25
bus_stops =10
time_per_stop =2

bus_time_taken = dist_to_uni / (bus_speed/60)
print(bus_time_taken)
for i in range(bus_stops):
    bus_time_taken += time_per_stop
print(f"It takes {bus_time_taken} minute to reach university by bus")

#for running

speed_1=7
speed_2=15
run_time_taken =0
for i in range (dist_to_uni):
    run_time_taken +=1/(speed_1/60 if i==0 or i==3 else  speed_2/60)

print(f"It takes {run_time_taken} minutes to reach university by jogging")

print(f"Its faster to run"if run_time_taken < bus_time_taken else "Its faster by bus ")