import random

l = map(int, raw_input().split())
rational = l[0]
correct = l[1]
check = l[2]
trial = 10000
list = ["correct"] * correct + ["rational"] * rational

count = 0
for _ in range(trial):
    i = True
    while i:
    	robot = random.sample(list,check)
	if robot.count("correct") > check/2:
	    i = False
    count += robot.count("rational")
print float(count)/trial
