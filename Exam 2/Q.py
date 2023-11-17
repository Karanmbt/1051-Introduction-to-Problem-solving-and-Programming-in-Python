def readOrders(filename):
    totalCost = 0.000
    data = open(filename, "r")
    for line in data:
        line_CSV = line.split(",")
        if line_CSV[0] != "Food":
            totalCost += line_CSV[2]
    return totalCost


file = "Exam 2\data.csv"
print(readOrders(file))
