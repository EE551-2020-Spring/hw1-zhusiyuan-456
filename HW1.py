Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def numbers_and_strings():
	x="EE551"
	y="Stevens"
	z=5*y
	length=len(z)
	m=y+" is good"
	n=m.replace("good","awesome")
	return x,y,z,length,m,n


>>> def list():
	n="Stevens is awesome"
	p=n.split(", ",17)
	r=p[3:-1]
	first_row=[1,4,5]
	second_row=[6,10,11]
	third_row=[12,17,38]
	c=('first_row[2]','second_row[2]','third_row[2]')
	(x,y,z)=c
	s = ("stevens") 
l1 = [] 
l2 = []
for c in s:  
    l1.append(c) 
    l2.append(ord(c))

	return p,r,c,o

 def dictionaries():
 a={"fruit":"apple","quantity":4,"color":"green"}
f=a["fruit"]
p={"first_name":"Grace",'last_name':'Hopper','jobs':['scientist','engineer'],'age':85}
p['jobs'].append("programmer")
return a,f,p
