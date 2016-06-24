bacteria_number = input ("What is the number of bacteria?")
bacteria_number = int (bacteria_number)
time = input ("What is the replication time?")
time = int (time)
if (time%2==0):
    total_bacteria = bacteria_number*(2**(time/2))
else:
    total_bacteria = bacteria_number*(2**((time-1)/2))
print ("After",time, "minutes, we would have", total_bacteria, "bacteria")
