from efuntions import*


##----##
#The input of the following problem are the images and the times
##----##


ls=['take1-06_40_59.png','take2-08_06_06.png','take5-13_10_41.png']

#We find the diferent radius radius 
r0,r1,r2 = radii(ls)
t1,t2 = abs((6+40/60+59/3600)-(8+6.0/60.0+6.0/3600)), abs((6+40.0/60+59.0/3600)-(13+10.0/40+41.0/3600))

#Here we find the angles of rotation 
th1,th2 = equation(r0,r1,r2,t1,t2)

#Finally we can graph
graph(r0,r1,r2,th1,th2)
