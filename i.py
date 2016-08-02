#AcgBag Lottery Software 
#please set a r.txt for source list
#and Please set a f.txt for output list
#By ShellV-Pro From AcgBag Software Team
#For dbacg.com by Apache licence 2.0
import time
import random
print "AcgBag Lottery Software"
start = time.clock()
list = []
for line in open("r.txt"):
	list.append(line)
print list
random.shuffle(list)
f = open('f.txt', 'w+')
f.writelines(list)
f.close()
end = time.clock()
print "We use: %f s for this event" % (end - start)