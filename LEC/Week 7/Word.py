text = open("LEC/Week 7/words5000.csv", "r")

#lines = text.readlines() #then ilerate over lines[1:]

for line in text:
    line = line.strip()
    Rank, Word, Part_of_speech, Frequency, Dispersion = line.split(",")
    print(Rank, Word, Part_of_speech, Frequency, Dispersion)