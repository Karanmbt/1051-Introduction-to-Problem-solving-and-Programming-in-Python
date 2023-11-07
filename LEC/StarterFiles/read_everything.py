#import time
target = open("hamlet.txt", "r",  encoding="utf8")
#for line in target:
#    print(line)
#    time.sleep(0.19)

#text = target.read()
#print(text)

text = target.readlines()
print(text[:100])