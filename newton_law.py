import sys,re
import time
import matplotlib.pyplot as plt

 
force = float(raw_input("enter the force you want to apply " +"N(Newton) "))
mass = float(raw_input("enter the mass in  Kg  "))
friction = float(raw_input("enter the frictional force apply by surface"+"N(Newton) "))
distance = float(raw_input("how much distance you want to cover(meter)  " ))

acceleration = (force-friction)/mass  # here we calculate how much acceleration(constant) will object get ,while applying continious constant force
print acceleration
fp = open('output.txt','w+')
fp.write("Acceleration due to force = %s meter/sec^2\n\n"%(str(acceleration)))

print("Time(sec)\t"+"  velocity\t"+" Distance_cover")

velocity = [0.0]
time1 = [0]
distance_list = [00.00]


def plotting_v(velocity,time1):
                plt.subplot(2,1,1)
                plt.axis([0,40,0,40])
		plt.scatter(time1[-1],velocity[-1])
		plt.pause(0.25)
		plt.grid(True)
		
		plt.xlabel("x--> time(sec)")
		plt.ylabel("y--> velocity(meter/sec)")
                

def plotting_d(distance_list,time1): 
                plt.subplot(2,1,2)
                plt.axis([0,30,0,distance])
		plt.scatter(time1[-1],distance_list[-1])
                plt.pause(0.25)
		plt.grid(True)
		plt.xlabel("x--> time(sec)")
                plt.ylabel("y--> Distance_cover(meter/sec)")
	
		
def velocity1(a):
		i = 0
		while True:
			time.sleep(.50)
			final_velocity = velocity[-1] + (acceleration * i)
			
			distance_cover = final_velocity + distance_list[-1]
			distance_list.append(distance_cover)
		

			velocity.append(final_velocity)
			i = i+1
                        time1.append(i)
                        
                       
			plotting_v(velocity,time1)
			plotting_d(distance_list,time1)	


                        print(str(time1[-2])+"\t\t"+str(velocity[-1])+"\t\t\t"+str(distance_list[-1]))

                        if distance_list[-1] >= distance or distance_list[-1] <= (distance - distance*2):
                                
                                text_file(time1,velocity,distance_list)
				break 


def text_file(time1,velocity,distance_list):
         fp.write("Time(sec.)"+"\tVelocity(m/s) "+"\tDistance(meter) \n")
         
         for i in range(len(time1)-1):
                fp.write('  '+str(time1[i]))
                fp.write('\t\t '+str(velocity[i+1]))
                fp.write('\t\t '+str(distance_list[i+1]))
                fp.write('\n')



def main():
        velocity1(acceleration)
        fp.close()   	
         
if __name__ == "__main__":
    main()

plt.show()
