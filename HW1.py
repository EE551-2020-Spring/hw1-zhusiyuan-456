
>>> import math
>>> def numbers_and_strings():
	x="EE551"
	y="Stevens"
	z=5*y
	length=len(z)
	m=y+" is good"
	n=m.replace("good","awesome")
	return x,y,z,length,m,n

def lists():
    n = "Stevens is awesome"
    p= n.split(' ')
    r=p[2][1:]
    A=[[1,4,5],[6,10,11],[12,17,38]]
    c =[row[2] for row in A]
    d=[A[i][2-i] for i in [0,1,2]if(A[i][2-i]%2==0)]
    o=[[i,ord(i)] for i in['S','t','e','v','e','n','s']]
    return p, r, c, d, o

 def dictionaries():
 a={"fruit":"apple","quantity":4,"color":"green"}
 f=a["fruit"]
 p={"first_name":"Grace",'last_name':'Hopper','jobs':['scientist','engineer'],'age':85}
 p['jobs'].append("programmer")
 return a,f,p
