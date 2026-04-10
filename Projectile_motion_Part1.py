#Preferably, use Jupyter notebook
#Projectile motion part 1 (2d and 3d visualization)

import time
from turtle import *
import math
from numpy import *
from scipy.integrate import quad
from matplotlib.pyplot import *
from mpl_toolkits import mplot3d

print("Projectile motion of an object on a particular celestial body")
print("")


def trajectory(v,a,g,h):
    """
    This function is for calculating the maximum height, time of impact, distance, and speed of impact in a projectile motion
    Input: initial velocity, angle of elevation, gravity of the celestial body, and height where the object lauched
    Output: maximum height, time of impact, distance, and speed of impact
    """
    r = a*(math.pi/180)
    h_max = (v*v)*(math.sin(r)*math.sin(r))/(2*g) + h
    t_impact = (v*math.sin(r)+math.sqrt(v*v*math.sin(r)*math.sin(r)+2*g*h))/g
    distance = v*math.cos(r)*t_impact
    s_impact = math.sqrt(v*v + 2*g*h)

    return h_max, t_impact, distance, s_impact, r





def trajectory_length(v,a,g,t_impact):
    """
    This function is for calculating the arc length of the given trajectory from time t = 0 to time of of impact to the surface
    Input: initial velocity, angle of elevation, gravity of the celestial body, and the time of impact to the surface
    Output: length of the trajectory
    """
    r = a*(math.pi/180)
    def f(t):
        return ((v*cos(r))**2+(v*sin(r)-g*t)**2)**(0.5)
    y = quad(f, 0, t_impact)
    
    return round(y[0],2)

print("Suppose that any air resistance of the celestial body is negligible.")
print("")
print("Enter the following: ")
print("")

obj = input("Name of the object: ")

print("")

celes = input("Name of the celestial body: ")
print("")
v = float(input("Initial velocity of "+obj+" (in m/s) v: "))
print("")
if v<=0 or v>=299792458:
    #Note that 299792458 m/s is the speed of light and no object can travel greater than or equal to that speed.
    print("Error!!!! 0<v<299792458")

else:
    a = float(input("Angle of elevation (The angle which "+obj+" is launched) (in degrees) (0<a<90) a: "))
    print("")
    if a<=0 or a>= 90:
        print("Error!!!! 0<a<90")
    else:
        g = float(input("Gravity of "+ celes+" (in m/s^2) g: "))
        print("")
        if g<=0: 
            print("Error!!!! g>0")
        else:
            h = float(input("Height (where " +obj+" is launched) (in meters) h: "))
            print("")
            if h<0:
                print("Error!!!! h>=0")
            else:
                print("Given:")
                print("")
                print("Initial velocity is "+str(v)+" m/s.")
                print("")
                print("The angle of elevation is "+str(a)+" degrees.")
                print("")
                print("Gravity of "+celes+" is "+str(g)+" m/s^2.")
                print("")
                print("The height where "+obj+" lauched is "+str(h)+" m.")
                print("")
                
                h_max, t_impact, distance, s_impact, r=trajectory(v,a,g,h)
                length = trajectory_length(v,a,g,t_impact)
                
                
                print("The results are: ")
                print("")
                print("The distance where the "+obj+" will land is "+str(round(distance,2))+" m.")
                print("")
                print("The maximum height that the "+obj+" can possibly reach is "+str(round(h_max,2))+" m.")
                print("")
                print("The speed of impact of the "+obj+" is "+str(round(s_impact,2))+" m/s.")
                print("")
                print("The time of impact of the "+obj+" to the surface is "+str(round(t_impact,2))+" s.")
                print("")
                print("The length of the trajectory is "+str(length)+" m") 
                
                %matplotlib notebook
                #For the visualization
                #####################################################################################################
                ###### 2D #######
                
                fig = figure(figsize=(7,7))
                title("The trajectory of "+obj+" on "+celes + " (2D)")
                t = arange(0, t_impact, 0.01)
                x = v*cos(r)*t
                y = v*sin(r)*t-(0.5)*g*t**2+h
                plot(x,y)
                
                t123 = v*sin(r)/g
                x123 = v*cos(r)*t123
                x143 = [x123,distance]
                y143 = [h_max,0]
                plot(x143,y143,"r*")
                
                y6 = [0,distance]
                x6 = [0,0]
                plot(y6,x6,"g")
                
                y8 = [0,0]
                x8 = [0,h]
                plot(y8,x8,"k")
                
                
                max1 = max(distance, h_max)
                if max1 == h_max:
                    xlim(-max1/2+x123,max1/2+x123)
                    ylim(-10,max1+30)
                else:
                    xlim(-10,max1+20)
                    ylim(-10,max1+30)
                grid()
                show()
                #####################################################################################################
                ###### 3D #######
                
                fig = figure(figsize=(7,7))
                ax = axes(projection = "3d")
                
                h1 = arange(0,h,0.1)
                z1 = h1
                x1 = 0*h1
                y1 = 0*h1
                ax.plot(x1,y1,z1,"k",linewidth = 5)
                
                t = arange(0, t_impact, 0.01)
                x = v*cos(r)*t
                y = v*sin(r)*t-(0.5)*g*t**2+h
                
                ax.plot(x,0*t,y,"r")
                ax.set_title("The trajectory of "+obj+" on "+celes+ " (3D) ")
                ax.set_xlabel("x-axis",labelpad=20)
                ax.set_ylabel("y-axis",labelpad=20)
                ax.set_zlabel("z-axis",labelpad=20)
                if max1 == h_max:
                    ax.set_xlim(-max1/2+x123,max1/2+x123)
                    ax.set_zlim(0,max1+30)
                    ax.set_ylim(-max1/2,max1/2)
                else:
                    ax.set_xlim(-10,max1+20)
                    ax.set_zlim(0,max1+30)
                    ax.set_ylim(-max1/2,max1/2)
               
                show()
