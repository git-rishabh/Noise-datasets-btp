import pickle
import math
import random

f=open("new_so_edges.txt","rb")
lines=f.readlines()
edges=dict()
for i in lines:
	row = i.split(" ")
	v1=row[0].strip()
	v2=row[1].strip()
	edge=(v1,v2)
	edges[edge]=1
# print edges
nodesList=set()
for i in edges.keys():
	nodesList.add(i[0])
	nodesList.add(i[1])

nodesList=list(nodesList)
print len(nodesList)
p=10
n=len(edges)
perc=math.floor((p*n)/100)

AddOnly=False
removeAndAdd=True
print p
print "no =  ",perc
print "Original Edges ",len(edges)

cnt=0
edgesList=list(edges)
print edgesList[0]

if(removeAndAdd):
	print "Remove and Add Noise"
	while(cnt<perc):
		if(cnt%100==0):
			print cnt,
		ind = random.choice(list(edges))
		# i1=random.randint(0,len(edgesList))
		# e=edgesList[i1]
		# v1=e[0].strip()
		# v2=e[1].strip()
		# ind=(v1,v2)
		del edges[ind]
		# edgesList.remove(ind)
		cnt=cnt+1
	print " "
	print "After Remove ",len(edges)

	cnt1=0
	print " "
	while(cnt1<perc):

		if(cnt1%100==0):
			print cnt1,
		i1=random.randint(0,len(nodesList))
		i2=random.randint(0,len(nodesList))
		v1=nodesList[i1]
		v2=nodesList[i2]
		while(v1==v2 or (v1,v2) in edges or (v2,v1) in edges):
			i1=random.randint(0,len(nodesList))
			i2=random.randint(0,len(nodesList))
			v1=nodesList[i1]
			v2=nodesList[i2]
		di=random.randint(0,10)
		if(di>5):
			edges[(v1,v2)]=1
		else:
			edges[(v2,v1)]=1
		
		cnt1=cnt1+1
	print " "
	print "After Add and Final ",len(edges)

	with open("noise2_"+str(p)+"_edges.dump", "wb") as fp2:   #Pickling
		pickle.dump(edges,fp2)

elif(AddOnly):
	print "Add Only Noise"

	cnt1=0
	while(cnt1<perc):
		if(cnt1%100==0):
			print cnt1,
		i1=random.randint(0,len(nodesList))
		i2=random.randint(0,len(nodesList))
		v1=nodesList[i1]
		v2=nodesList[i2]
		while(v1==v2 or (v1,v2) in edges or (v2,v1) in edges):
			i1=random.randint(0,len(nodesList))
			i2=random.randint(0,len(nodesList))
			v1=nodesList[i1]
			v2=nodesList[i2]
		di=random.randint(0,10)
		if(di>5):
			edges[(v1,v2)]=1
		else:
			edges[(v2,v1)]=1
		
		cnt1=cnt1+1
	
	print " "
	
	print "After Add and Final ",len(edges)

	with open("noise1_"+str(p)+"_edges.dump", "wb") as fp2:   #Pickling
		pickle.dump(edges,fp2)

# p=15
# name="noise2_"+str(p)+"_edges"
# with open("noise2_"+str(p)+"_edges.dump", "rb") as fp2:   #Pickling
# 		ed = pickle.load(fp2)
# f11=open(name+".txt","wb")

# for k in ed.keys():
# 	v1=k[0]
# 	v2=k[1]
# 	f11.write(v1+" "+v2+"\n")

# f11.close()
