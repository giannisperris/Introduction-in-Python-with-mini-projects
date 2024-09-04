import statistics

with open('inputdata.txt', 'r') as infile:
    data = infile.readlines()

values = [float(line.strip()) for line in data]
mean_value = statistics.mean(values)
stdev_value = statistics.stdev(values)

with open('outputdata.txt', 'w') as outfile:
    outfile.write(f"Μέσος όρος: {mean_value:.3f}\n")
    outfile.write(f"Τυπική απόκλιση: {stdev_value:.3f}\n")

print("Τα αποτελέσματα αποθηκεύτηκαν στο outputdata.txt.")