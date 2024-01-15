# Q5

import re

def redact(filename):
    file = open(filename, "r")
    newFile = open("Final Exam/redacted.txt", "w")
    for line in file:
        line = re.sub(r"([A-Z]{2,3}-\d{4}-\d{4}-\d{4})", "REDACTED", line)
        line = re.sub(r"([A-Z]{2,3}-\d{12})", "REDACTED", line)
        newFile.write(line)
    file.close()
    newFile.close()
    
redact("Final Exam\insuricareinput.txt")
