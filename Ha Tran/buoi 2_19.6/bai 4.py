initial_number=int(input("Initial B bacteria number : "))
time=float(input("Period of time : "))
total_B=int(initial_number*(2**(time//2)))
print("After ",time," minutes we would have",total_B," bacteria(s)")
