#read words5000.csv file and store the contents into five lists. 
text = open("LEC/Week 7/words5000.csv", "r")

lines =  text.readlines()  # then iterate over lines[1:]
rank = []
word = []
part = []
freq = []
disp = []
for line in lines[1:]:
    line = line.strip()
    #word.append(
    cols = line.split(",")
    rank.append(cols[0])
    word.append(cols[1])
    part.append(cols[2])
    freq.append(cols[3])
    disp.append(cols[4])
print(word)