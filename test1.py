import matplotlib.pyplot as plt
import numpy as np

k = 1 #spring constant
m = 1 #mass of object
w = 1 #frequency of oscillation
dt = [0.1, 0.5, 1] #time step
total_time = 50
t = int(total_time/dt) #number of time intervals
x0 = 2 #Initialise Conditions
v0 = 1 #Initialise Conditions

##Initialise vector arrays##
#time = np.linspace(0, total_time, t)
x = np.zeros(t) #Position
v = np.zeros(t) #Velocity
time = np.zeros(t)

x[0] = x0 #Initial Conditions
v[0] = v0 - 0.5*dt #Initial Conditions

time[0] = 0
##Leapfrog Method Solver##
for j in xrange():
    for i in xrange(t-1):
        v[i + 1] = v[i] - dt*x[i]*w**2 #Velocity Calculation
        x[i + 1] = x[i] + dt*v[i + 1] #Position Calculation
        time[i + 1] = (i + 1) * dt #Time step calculation

##Analytical Solution##
y = x0 * np.cos(w*time) + ((v0/w)* np.sin(w*time))

#L^2 Error Norm
ErrorNorm = np.sqrt(sum(((x - y)**2)/x**2))

## Plot Graphs ##
Leapfrog,  = plt.plot(time, x, label = 'Leapfrog')
Analytical, = plt.plot(time, y, label = 'Analytical')
plt.legend()
plt.xlabel('Time')
plt.show()
#plt.plot(, ErrorNorm)
