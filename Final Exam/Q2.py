# Q2

def brainToBody(filename):
    file = open(filename, "r")
    maxratio = 0
    maxanml = ""
    for line in file:
        line = line.strip()
        line = line.split(",")
        ratio = float(line[2]) / float(line[1])
        if ratio > maxratio:
            maxratio = ratio
            maxanml = line[0]
    return maxanml


print(brainToBody("Final Exam/animals.csv"))
