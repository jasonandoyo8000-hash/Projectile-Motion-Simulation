#Projectile motion part 2
#Simulation using turtle graphics
#Continuation of part 1 

def write_message(message, x, y, size):
    """
    This function is for writing a message at point (x,y)
    Input: message, x-component, y-component, font size
    Output: show the message at point (x,y) with a specific size
    """
    penup()
    goto(x, y)
    pendown()
    color("black")
    write(message, align="center", font=("Times", size, "bold"))
    penup()
title("Trajectory of "+obj+" on "+celes)
bgcolor("lightblue")
                
f = 1
while f==1:
    speed(0)
    width(2)
    hideturtle()
    penup()

    color("black")
    begin_fill()
    fillcolor("green")
    goto(700,-200)
    pendown()
    goto(-700,-200)
    goto(-700,-500)
    goto(700,-500)
    goto(700,-200)
    end_fill()

    write_message(celes, 0, -270, 18)

    mean = (h_max+distance)/2
    goto((1/mean)*(-100*distance)+5,-200)
    color("black")
    begin_fill()
    fillcolor("gray")
    goto((1/mean)*(-100*distance)+5,(1/mean)*(200*h)-200)
    goto((1/mean)*(-100*distance)-10,(1/mean)*(200*h)-200)
    goto((1/mean)*(-100*distance)-10,-200)
    goto((1/mean)*(-100*distance)+10,-200)
    end_fill()
    penup()
    goto((1/mean)*(-100*distance),(1/mean)*(200*h)-200)

    color("blue")
    pendown()
    for t in arange(0,t_impact,t_impact/350):
        x = (v*cos(r))*t
        y = v*sin(r)*t-(0.5)*g*t**2+h
        goto((1/mean)*(200*x-100*distance),(1/mean)*(200*y)-200)
    goto((1/mean)*(100*distance),-200)
    write_message("height: "+str(round(h,2))+" m",(1/mean)*(-100*distance)-20,(1/mean)*(200*h)-200,8)
    write_message("maximum height: "+str(round(h_max,2))+" m",0,(1/mean)*(200*h_max)-190,8)
    write_message("length of the trajectory: "+str(length)+" m",0,(1/mean)*(200*h_max)-177,8)
    write_message("speed of impact: "+str(round(s_impact,2))+" m/s",(1/mean)*(100*distance),-212,8)
    write_message("time of impact: "+str(round(t_impact,2))+" s",(1/mean)*(100*distance),-225,8)
    write_message("distance: "+str(round(distance,2))+" m",(1/mean)*(100*distance),-238,8)
    time.sleep(5)
    clear()
