#!/usr/bin/env python

"""
Solar System Simulator

https://www.astro.rug.nl/~oberg/python.html
https://www.astro.rug.nl/~oberg/orbit_test_016_pretty.py
https://www.astro.rug.nl/~oberg/ejected.png

"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

#from orbital import earth, mercury, venus, jupiter, saturn, uranus, neptune, KeplerianElements, Maneuver, plot
#from sun_body import sun

start_total = time.time()

## constants ######################################

G = 6.67E-11 #[m^3 kg^-1 s^-2]
mu = G*1988550000E21
AU = 149597870700

## variables ######################################

TIME = input("Time [days]: ")               #seconds
NUM = input("Number of asteroids: ")    #number of asteroids
ECC = 0                              #surface density power law for asteroids
HEIGHT = 1                           #scale height for asteroids
STEP = 86400/2                         #stepsize
N = 1

## user input #####################################

lagrange = input("Spawn asteroids at L4?  0 = no, 1 = yes. ")                          
just_jupiter = input("Move only Jupiter? 0 = no, 1 = yes.")
co_rotate = input("Create Jupiter rotation plot? 0 = no, 1 = yes.")
real_greek = input("Override and use asteroid 1134_Odysseus instead? 0 = no, 1 = yes.")

## planets ########################################

# planet index legend
#
# [0] = mass [kg]
# ---
# [1] = SMA [m]
# [2] = eccentricity 
# [3] = longitude ascending node
# [4] = argument of perihelion 
# [5] = inclination 
# [6] = mean anomaly [radians]
# ---
# [7] = position [r[m],theta,phi]
# [8] = velocity [[m/s],[m/s],[m/s]]

Helios = [1988550000E21, 
    0,
    0,
    0,
    0,
    0,
    0,
    [0,0,0],
    [0,0,0]]

Hermes = [330.2E21,                                                     
    0.38709893*1.496E11,                                                
    0.20563069,                                                          
    np.radians(48.33167),                                               
    np.radians(77.45645),                                               
    np.radians(7.00487),                                                
    np.radians(174.796),                                                
    [69784286384.059692, 1.6882673124901941, -1.0093434814812288],      
    [38881.915595717335, 1.6063671453406956, 0.5497171832548039]]       

Aphrodite = [4868.5E21,
    0.72333199*1.496E11,
    0.00677323, 
    np.radians(76.68069), 
    np.radians(131.53298),
    np.radians(3.39471),
    np.radians(50.115),
    [107743414541.8663, 1.5731177516529296, 1.3774756378596795],
    [35171.887066621879, -1.630010923175951, -0.19841223943418446]]

Gaia = [5973.6E21,
    1.00000011*1.496E11, 
    0.01671022, 
    np.radians(-11.26064),
    np.radians(102.94719),
    np.radians(0.00005),
    np.radians(358.617),
    [147100920445.17923, 1.570795471700897, -1.5663221885112795],
    [30286.259644601396, 1.5707965013805607, 0.0048843579226186488]] 

Ares = [641.85E21,
    1.52366301*1.496E11, 
    0.09341233, 
    np.radians(49.57854), 
    np.radians(336.04084),
    np.radians(1.85061),
    np.radians(19.373), 
    [208104578760.48801, 1.5711353952155658, 0.85481449702703571],
    [26328.96746448768, -1.5385292139075961, -0.75010717966548468]]

Zeus = [1898600E21,
    5.2033630*1.496E11, 
    0.04839266, 
    np.radians(100.55615),
    np.radians(14.75385), 
    np.radians(1.30530),
    np.radians(20.020),
    [743258531323.42432, 1.5571547187024335, -0.74464453998332747],
    [13660.927, 1.55231, 0.809027]]

Cronus = [568460E21,
    9.53707032*1.496E11, 
    0.05415060, 
    np.radians(113.71504),
    np.radians(92.43194),
    np.radians(2.48446),
    np.radians(317.020),
    [1372287903624.4966, 1.5401362627414401, -0.37185520925680393],
    [10019.989822296526, 1.5413444120879047, 1.2383284929872507]]

Ouranos =  [86832E21,
    19.19126393*1.496E11,
    0.04716771,
    np.radians(74.22988),
    np.radians(170.96424),
    np.radians(0.76986),
    np.radians(142.238),
    [2980336794232.105, 1.5800686098692218, 0.5339904135612229],
    [6544.7486685107297, -1.5613341304368002, -1.0647556186729656]]

Poseidon = [102430E21,
    30.0689634*1.496E11,
    0.00858587, 
    np.radians(131.72169),
    np.radians(44.97135), 
    np.radians(1.76917),
    np.radians(256.228),
    [4507823064520.3955, 1.5974696457828985, 1.2562849510340699],
    [5420.1712839989968, -1.5550230345576961, -0.30660640388486443]] 

solar_system = [Hermes,Aphrodite,Gaia,Ares,Zeus,Cronus,Ouranos,Poseidon]

## real asteroids ###############################

Odysseus_1143 = [0,
    5.20256*AU,
    0.0594801228345, 
    np.radians(168.488315803),
    np.radians(314.303166925), 
    np.radians(0.92038274215),
    np.radians(204193.753008),
    [837292847430.94788, 1.5539060304008383, 1.0339067744004882],
    [-12165.748317494808, 1.5177793114245315, -0.59647137477285761]] 

# planet index legend
#
# [0] = mass [kg]
# ---
# [1] = SMA [m]
# [2] = eccentricity 
# [3] = longitude ascending node
# [4] = argument of perihelion 
# [5] = inclination 
# [6] = mean anomaly [radians]
# ---
# [7] = position [r[m],theta,phi]
# [8] = velocity [[m/s],[m/s],[m/s]]


asteroids = [] 

## functions ############################

## Convert cartesian to spherical coordinates. 
def cart_to_sphere(pos):
#    pos = orbit.r
    xpos = pos[0]
    ypos = pos[1]
    zpos = pos[2]
    r_pos = np.sqrt(xpos**2 + ypos**2 + zpos**2)
    phi_pos = np.pi + np.arctan2(-1*ypos, -1*xpos)
    theta_pos = np.arctan(np.sqrt(xpos**2 + ypos**2)/zpos)
    position = [r_pos, theta_pos, phi_pos]
    return position


## Convert spherical to cartesian coordinates. 
def sphere_to_cart(r,t,p):
    x = r * np.sin(t) * np.cos(p)
    y = r * np.sin(t) * np.sin(p)
    z = r * np.cos(t)
    return [x,y,z]


## Creates pseudo-random radius for nth asteroid in function call loop.  
## Radii distributed by power law with shape parameter 3.5.  Asteroids
## do not appear inside inner radius 0.5 AU.
def astr_init_radius(N):
    radii = []
    distrib = []
    distance_num = 50*149597870700   #[50 AU in meters]  
    inner_radius = 0.5*149597870700  #[0.1 AU in meters]
    shape_parameter = 3.5 
    temp_distrib = np.random.power(shape_parameter, N)
    for i in range(len(temp_distrib)):
        temp_distrib[i] = 1-temp_distrib[i]
        distrib.append(temp_distrib[i])
    for j in range(len(distrib)):
        radius = distance_num * distrib[j]
        radius += inner_radius
        radii.append(radius)
    return radii


## Creates pseudo-random theta (angle relative to z axis) value for asteroid 
## with gaussian spread with center np.pi/2 (in ecliptic) with 
## sigma = 0.01 radians. 
def astr_init_theta(N): 
    thetas = [np.random.normal(loc = np.pi/2, scale=0.01)] #[np.pi/2] 
    return thetas


## Creates random phi value (angle relative to x axis) for asteroid on interval
## 0 to 2*pi radians.
def astr_init_phi(N):
    phis =  [np.random.uniform(0, 2*np.pi)]
    return phis


## Substitute function for random asteroid positions.  Generates radius, theta
## and phi values which place asteroids near Jupiter L4.
def trojans(n):
    radius = [np.random.normal(loc = 5.2*AU, scale=0.1*AU)]
    theta = [np.random.normal(loc = np.pi/2, scale=0.01)] 
    phi =  [(-0.744644 + np.pi/3)*np.random.normal(loc = 1, scale=0.1)]
    #the following values are for testing
    #radius = [780264673251.9336]
    #theta = [1.5703887563134749]
    #phi =  [0.2564734217839243-0.01*7+0.001+0.001*n]
    return radius,theta,phi


## Substitute function for random asteroid velocities.  Generates radius, theta
## and phi velocity vector values.
def trojans_v(radius,theta,phi,n):
    theta_vec = [(np.pi/2 )*np.random.uniform(0.95,1.05)]
    radial_vec =  [np.sqrt((G * Helios[0]) / radius[0])]
    phi_vec = [(phi[0] + (np.pi/2))*np.random.uniform(0.95,1.05)] 
    velocity_vec = [[radial_vec[0],theta_vec[0],phi_vec[0]]]
    #the following values are for testing
    #velocity_vec = [[13046.339635174816,1.525528799663296,1.8364033055616142]]
    return velocity_vec 


## Creates pseudo-random initial velocity vector [r,theta,phi] for asteroids.
## Radial values are based on spherical orbital velocities.
## Theta values are spread about pi/2 (ecliptic plane) on uniform interval 0.9-1.1
## Phi values are spread about Jupiter phi + pi/3 radians on uniform interval 0.8-1.2
def astr_init_velocities(radius,theta,phi):
    theta_vec = [(np.pi/2 )*np.random.uniform(0.9,1.1)]
    radial_vec =  [np.sqrt((G * Helios[0]) / radius[0])]
    phi_vec = [(phi[0] + (np.pi/2))*np.random.uniform(0.8,1.2)] 
    velocity_vec = [[radial_vec[0],theta_vec[0],phi_vec[0]]]
    return velocity_vec 


## Combines all initial position and velocity vectors for an asteroid.
## Call function[0] for position vector, function[1] for velocity vector
## If user specifies lagrange == 1, the function will limit the asteroid
## distribution to the trojans() and trojans_v() functions.
def astr_init_combo(n):
    if lagrange == 0:
        position_vec = []
        radius = astr_init_radius(N)
        theta = astr_init_theta(N)
        phi = astr_init_phi(N)
        velocity_vec = astr_init_velocities(radius,theta,phi) 
        for i in range(len(radius)):
            position_vec.append([radius[i],theta[i],phi[i]])
        return [position_vec,velocity_vec]
    else:
        position_vec = []
        radius,theta,phi = trojans(n)
        velocity_vec = trojans_v(radius,theta,phi,n) 
        for i in range(len(radius)):
            position_vec.append([radius[i],theta[i],phi[i]])
        return [position_vec,velocity_vec]


## Calculates difference between two 3D cartesian coordinates.
## Call function[0] for dx, function[1] for dy, function[2] for dz.
def dxyz(m1,m2): 
    dx = m2[0]-m1[0]
    dy = m2[1]-m1[1]
    dz = m2[2]-m1[2]   
    return dx,dy,dz


## Calculates distance between two 3D cartesian coordinates.
def d(m1,m2): 
    dx,dy,dz = dxyz(m1,m2) 
    distance = np.sqrt(dx**2+dy**2+dz**2) 
    return distance


## Returns direction vector pointing from object m1 to m2.
def direction(m1,m2): 
    xd,yd,zd = dxyz(m1,m2)
    vector = np.array((xd,yd,zd)/d(m1,m2))
    return vector    


## Calculates changes in position and velocity vector of asteroid
## using acceleration given by a = F/m1 where F = G*m1*m2/r**2
## Forces are computed for the Sun, Jupiter, Saturn, Uranus, and Neptune.
## Call function[0] for position vector, function[1] for velocity vector.
def newton(body,t):
    pos_xyz = body[0][0]
    vel_xyz = body[1][0]
    a = G*Helios[0]/(d(pos_xyz,[0,0,0])**2)
    a += G*Zeus[0]/(d(pos_xyz,Zeus[7])**2) 
    a += G*Cronus[0]/(d(pos_xyz,Cronus[7])**2) 
    a += G*Ouranos[0]/(d(pos_xyz,Ouranos[7])**2) 
    a += G*Poseidon[0]/(d(pos_xyz,Poseidon[7])**2) 
    vel_xyz += a * t * direction(pos_xyz,[0,0,0])  
    pos_xyz += vel_xyz * t 
    return pos_xyz,vel_xyz 


## Function idential to newton() but considers only gravitational attraction
## due to the sun. Call function[0] for position vector, function[1] for 
## velocity vector.
def newton_for_planets(body,t):
    pos_xyz = body[0][0]
    vel_xyz = body[1][0]
    a = G*Helios[0]/(d(pos_xyz,[0,0,0])**2)
    vel_xyz += a * t * direction(pos_xyz,[0,0,0])  
    pos_xyz += vel_xyz * t   
    return pos_xyz,vel_xyz 


## Calculates full set of 6 classical orbital elements given cartesian state vectors.
## Argument 1 must be [r_x,r_y,r_z], argument 2 must be [v_x,v_y,v_z]
## function[0], a = semi-major axis [m]
## function[1], e = eccentricity
## function[2], small_o = argument of periapsis [radians]
## function[3], big_o = longitude of ascending node [radians]
## function[4], i = inclination [radians]
## function[5], M = mean anomaly [radians]
def analysis_OE(r,v):
    r[0] = float(r[0])
    r[1] = float(r[1])
    r[2] = float(r[2])
    v[0] = float(v[0])
    v[1] = float(v[1])
    v[2] = float(v[2])
    mag_r = magnitude(r)
    mag_v = magnitude(v)
    h = np.cross(r,v)
    n = np.cross(np.transpose([0,0,1]),h)
    mag_n = magnitude(n)
    e = (np.cross(v,h)/mu) - (r/mag_r)
    mag_e = magnitude(e)
    a = 1/((2/mag_r)-((mag_v**2)/mu))
    if e[2] >= 0:
        small_o = np.arccos(np.dot(n,e)/(mag_n*mag_e))
    else:
        small_o = 2*np.pi - np.arccos(np.dot(n,e)/(mag_n*mag_e))
    i = np.arccos(h[2]/magnitude(h))
    if n[1] >= 0:
        big_o = np.arccos(n[1]/mag_n)
    else:
        big_o = 2*np.pi - np.arccos(n[1]/mag_n)
    if np.dot(r,v) >= 0:
        nu = np.arccos(np.dot(e,r)/(mag_e*mag_r))
    else:
        nu = 2*np.pi - np.arccos(np.dot(e,r)/(mag_e*mag_r))
    E = 2*np.arctan(np.tan(nu/2) / np.sqrt((1+mag_e)/(1-mag_e)))
    M = E-mag_e*np.sin(E)
    return a,mag_e,small_o,big_o,i,M


## Efficient calculation of magnitude of cartesian vector [x,y,z]
def magnitude(x):
    m = np.sqrt(sum(i**2 for i in x))
    return m
    

## Rotates a cartesian [x,y] coordinate about angle phi [radians].
def rotate(phi,x,y):
    rx = x*np.cos(phi) - y*np.sin(phi)
    ry = x*np.sin(phi) + y*np.cos(phi)
    return rx,ry


## initial conditions ################################

pos_xyz = []
vel_xyz = []
planet_pos_xyz = []
planet_vel_xyz = []

#             P| N| 
#             O| O|
#             S| T|  
#             &| H|
#             V| I| X
#             E| N| Y
#             L| G| Z 
#asteroids[n][0][0][0]

print "-------------------------------------------------------------------"
print "Creating asteroids"
start = time.time()

## In this loop the n asteroids are created.  If the user specifies to use a real asteroid the
## random asteroids are not generated.  
if real_greek == 1:   
    pos_xyz.append(sphere_to_cart(Odysseus_1143[7][0],Odysseus_1143[7][1],Odysseus_1143[7][2]))
    vel_xyz.append(sphere_to_cart(Odysseus_1143[8][0],Odysseus_1143[8][1],Odysseus_1143[8][2]))
    asteroids.append([pos_xyz,vel_xyz])
else:
    for n in range(0,NUM):
        asteroid = astr_init_combo(n)
        asteroids.append(asteroid)
        pos_xyz.append(sphere_to_cart(asteroids[n][0][0][0],asteroids[n][0][0][1],asteroids[n][0][0][2]))
        vel_xyz.append(sphere_to_cart(asteroids[n][1][0][0],asteroids[n][1][0][1],asteroids[n][1][0][2]))
        print "Asteroid ", n+1 ,"/", NUM, "created."

stop = time.time() 
print "Completed creating asteroids ### ", "Elapsed time: ", stop-start, 's'
print "-------------------------------------------------------------------"

## Here initial planet positions are converted to cartesian coordinates and stored for the newton function.
for p in range(0,len(solar_system)):
    planet_pos_xyz.append(sphere_to_cart(solar_system[p][7][0],solar_system[p][7][1],solar_system[p][7][2]))
    planet_vel_xyz.append(sphere_to_cart(solar_system[p][8][0],solar_system[p][8][1],solar_system[p][8][2]))

## Here most arrays are created for plotting purposes.  Arrays are of the form
## [n1 n2 n3] where n is the nth asteroid and t is the time.
## [t1 t1 t1] In the array[n][t] index either the [x,y,z] position
## [t2 t2 t2] or velocity is stored. So array[0][100][0] would be the 
## x position of the 0th asteroid at time 100. 

plot_x =  np.array([[0. for i in range(NUM)] for j in range(TIME)]) 
plot_y = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_z = np.array([[0. for i in range(NUM)] for j in range(TIME)])

plot_x_v =  np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_y_v = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_z_v = np.array([[0. for i in range(NUM)] for j in range(TIME)])

plot_rx = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_ry = np.array([[0. for i in range(NUM)] for j in range(TIME)]) 

plot_planet_rx = np.array([[0. for i in range(NUM)] for j in range(TIME)]) 
plot_planet_ry = np.array([[0. for i in range(NUM)] for j in range(TIME)]) 

plot_planet_x =  np.array([[0. for i in range(len(solar_system))] for j in range(TIME)])
plot_planet_y =  np.array([[0. for i in range(len(solar_system))] for j in range(TIME)])
plot_planet_z =  np.array([[0. for i in range(len(solar_system))] for j in range(TIME)])

plot_planet_x_v =  np.array([[0. for i in range(len(solar_system))] for j in range(TIME)])
plot_planet_y_v =  np.array([[0. for i in range(len(solar_system))] for j in range(TIME)])
plot_planet_z_v =  np.array([[0. for i in range(len(solar_system))] for j in range(TIME)])

plot_sma  = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_ecc  = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_small_o = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_big_o = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_inc = np.array([[0. for i in range(NUM)] for j in range(TIME)])
plot_M = np.array([[0. for i in range(NUM)] for j in range(TIME)])

## physics ###########################################
print "Calculating Orbits"
start = time.time()

## In these loops, asteroid and planet positions are computed at each time step for n asteroids and 
## all planets.  If the user specifies just_jupiter == 1, only Jupiter's movement is considered.  
## All calculated values are stored into the plot_* arrays at this time.
for t in range(0,TIME):
    if just_jupiter == 1:
        solar_system[4][7],solar_system[4][8] = newton_for_planets(([planet_pos_xyz[4]],[planet_vel_xyz[4]]),STEP)
        planet_pos_xyz[4] = solar_system[4][7]
        planet_vel_xyz[4] = solar_system[4][8]
        plot_planet_x[t][4] = solar_system[4][7][0]
        plot_planet_y[t][4] = solar_system[4][7][1]
        plot_planet_z[t][4] = solar_system[4][7][2] 
        plot_planet_x_v[t][4] = solar_system[4][8][0]
        plot_planet_y_v[t][4] = solar_system[4][8][1]
        plot_planet_z_v[t][4] = solar_system[4][8][2]
    else:
        for p in range(0,len(solar_system)):
            solar_system[p][7],solar_system[p][8] = newton_for_planets(([planet_pos_xyz[p]],[planet_vel_xyz[p]]),STEP)
            planet_pos_xyz[p] = solar_system[p][7]
            planet_vel_xyz[p] = solar_system[p][8]
            plot_planet_x[t][p] = solar_system[p][7][0]
            plot_planet_y[t][p] = solar_system[p][7][1]
            plot_planet_z[t][p] = solar_system[p][7][2] 
            plot_planet_x_v[t][p] = solar_system[p][8][0]
            plot_planet_y_v[t][p] = solar_system[p][8][1]
            plot_planet_z_v[t][p] = solar_system[p][8][2]
    for n in range(0,NUM):
        temp_asteroid = [[0,0,0],[0,0,0]]
        temp_asteroid[0],temp_asteroid[1] = newton(([pos_xyz[n]],[vel_xyz[n]]),STEP)
        asteroids[n][0][0] = temp_asteroid[0]
        asteroids[n][1][0] = temp_asteroid[1]
        pos_xyz[n] = temp_asteroid[0]
        vel_xyz[n] = temp_asteroid[1]
        plot_x[t][n] = asteroids[n][0][0][0]
        plot_y[t][n] = asteroids[n][0][0][1]
        plot_z[t][n] = asteroids[n][0][0][2]
        plot_x_v[t][n] = asteroids[n][1][0][0]
        plot_y_v[t][n] = asteroids[n][1][0][1]
        plot_z_v[t][n] = asteroids[n][1][0][2]
    if np.remainder(t,10000) == 0:
        print int(100*t/TIME),'%'

print "100%"
stop = time.time()   
print "Simulation Complete ### ","Elapsed time: ", stop-start, 's'
print "-------------------------------------------------------------------"


## orbital elements ################################################
print "Computing Orbital Elements"
start = time.time()

## Here the 6 (keplerian) classical orbital elements are computed.  
for t in range(0,TIME):
    for n in range(0,NUM):
        sma,ecc,small_o,big_o,inc,M =  analysis_OE([plot_x[t][n],plot_y[t][n],plot_z[t][n]],[plot_x_v[t][n],plot_y_v[t][n],plot_z_v[t][n]]) 
        plot_sma[t][n] = float(sma)
        plot_ecc[t][n] = float(ecc)
        plot_small_o[t][n]  = float(small_o)
        plot_big_o[t][n]  = float(big_o)
        plot_inc[t][n] = float(inc)
        plot_M[t][n] = float(M)
    if np.remainder(t,10000) == 0:
        print int(100*t/TIME),'%'

print "100%"
stop = time.time()     
print "Completed Orbital Elements ### ", "Elapsed time: ", stop-start, 's'
print "-------------------------------------------------------------------"

## plotting #########################################################

temp_range = xrange(0,TIME,1) #range of time values for plotting purposes

frame1 = plt.subplot(1, 1, 1, projection='3d')  #3D plot frame

frame2 = plt.figure()                           #orbital elements frame1
ax2 = frame2.add_subplot(2, 1, 1)
ax3 = frame2.add_subplot(2, 1, 2)

frame4 = plt.figure()				#orbital elements frame2
ax5 = frame4.add_subplot(2, 1, 1)		
ax6 = frame4.add_subplot(2, 1, 2)

frame5 = plt.figure()				#orbital elements frame3
ax7 = frame5.add_subplot(2, 1, 1)
ax8 = frame5.add_subplot(2, 1, 2)

frame3 = plt.figure()                           #Jupiter rotation plot
ax4 = frame3.add_subplot(1,1,1)
 
frame6 = plt.figure()                           #orbital elements frame4
ax9 = frame6.add_subplot(1,1,1)

## Here every 1/5 [x,y,z] positions of n asteroids is plotted in 3D.
## Final locations of objects are included as a scatter plot.
for n in range(0,NUM):
    frame1.plot(plot_x[0::5,n]/AU,plot_y[0::5,n]/AU,plot_z[0::5,n]/AU,color='k',alpha=0.5)
    frame1.scatter(plot_x[-1][n]/AU,plot_y[-1][n]/AU,plot_z[-1][n]/AU,color='k',alpha=0.5) 

## Here every 1/5 [x,y,z] positions of planets are plotted in 3D.
## Final locations of objects are included as a scatter plot.
for p in range(0,len(solar_system)):
    frame1.plot(plot_planet_x[0::5,p]/AU,plot_planet_y[0::5,p]/AU,plot_planet_z[0::5,p]/AU,alpha=0.5) 
    frame1.scatter(plot_planet_x[-1][p]/AU,plot_planet_y[-1][p]/AU,plot_planet_z[-1][p]/AU,color='b')

## Plotting the location of the sun.
frame1.scatter(Helios[7][0],Helios[7][0],Helios[7][0],color='y',marker='*')

## If the user specifies co_rotate == 1 then this plot will be created where the entire coordinate system 
## rotates together with the current phi angle of Jupiter in its orbit.  The intent of this plot is to
## identify Greek and Trojan asteroids which librate about the Jupiter L4 point (indicated by a scatter point).
if co_rotate == 1: 
    for t in range(0,TIME):
        planet_pos = [plot_planet_x[t,4],plot_planet_y[t,4],plot_planet_z[t,4]]
        phi = cart_to_sphere(planet_pos)[2]
        for n in range(0,NUM): 
            rx,ry = rotate(-1*phi,plot_x[t][n],plot_y[t][n])
            plot_rx[t][n] = rx
            plot_ry[t][n] = ry   
    for n in range(0,NUM):
        ax4.plot(plot_rx[:,n],plot_ry[:,n],alpha=0.5,color='k') 
        ax4.scatter(plot_rx[-1][n],plot_ry[-1][n],alpha=0.5,color='k') 
    #for p in range(0,len(solar_system)):
    #    ax4.plot(plot_planet_rx[:,n],plot_planet_ry[:,n],alpha=0.5,color='k') 
    ax4.scatter(0,0) 
    ax4.scatter(5.2*AU*np.cos(np.pi/3),5.2*AU*np.sin(np.pi/3))

## plot orbital elements
for n in range(0,NUM):
    ax2.plot(temp_range,plot_ecc[:,n],label='eccentricity',alpha=0.8,color='k')
    ax3.plot(temp_range,plot_sma[:,n]/AU,label='semi-major axis',alpha=0.8,color='k')
    ax5.plot(temp_range,plot_small_o[:,n]/AU,label='argument of periapsis',alpha=0.8,color='k')
    ax6.plot(temp_range,plot_big_o[:,n]/AU,label='longitude of ascending node',alpha=0.8,color='k')  
    ax7.plot(temp_range,plot_inc[:,n]/AU,label='inclination',alpha=0.8,color='k')
    ax8.plot(temp_range,plot_M[:,n]/AU,label='mean anomaly',alpha=0.8,color='k')
    ax9.scatter(plot_sma[-1][n]/AU,plot_ecc[-1][n],alpha=1,color='k')
    ax9.scatter(plot_sma[0][n]/AU,plot_ecc[0][n],alpha=0.2,color='k')
    ax9.plot(plot_sma[:,n]/AU,plot_ecc[:,n],alpha=0.4,color='k')

## plot formatting
frame1.set_xlabel('[AU]')
frame1.set_ylabel('[AU]')
frame1.set_zlabel('[AU]')
frame1.set_xlim3d(-10,10)
frame1.set_ylim3d(-10,10)
frame1.set_zlim3d(-10,10)

ax2.set_xlabel("time [days]")
ax2.set_ylabel("eccentricity")
ax3.set_xlabel("time [days]")
ax3.set_ylabel("semi-major axis [AU]")

ax4.set_title("Co-rotating Jupiter Frame")
ax4.set_xlabel("position [m]")
ax4.set_ylabel("position [m]")

ax5.set_xlabel("time [days]")
ax5.set_ylabel("argument of periapsis")
ax6.set_xlabel("time [days]")
ax6.set_ylabel("longitude of ascending node")

ax9.set_xlabel("a [AU]")
ax9.set_ylabel("e")


#ax7.set_xlabel("time [days]")
#ax7.set_ylabel("inclination")
#ax8.set_xlabel("time [days]")
#ax8.set_ylabel("mean anomaly")

stop_total = time.time()
print "Total Elapsed time" , stop_total - start_total, 's'

plt.legend()
plt.grid()
plt.show()

## In this section the orbital python module was used to deterime state vectors 
## for the planets based on J2000 epoch classical orbital elements.  This only had to 
## be called once for initial conditions and so remains commented out.

#orbit0 = KeplerianElements(a=Helios[1],e=Helios[2],i=Helios[5],raan=Helios[3],arg_pe=Helios[4],M0=Helios[6],body=jupiter)
#orbit1 = KeplerianElements(a=Hermes[1],e=Hermes[2],i=Hermes[5],raan=Hermes[3],arg_pe=Hermes[4],M0=Hermes[6],body=sun)
#orbit2 = KeplerianElements(a=Aphrodite[1],e=Aphrodite[2],i=Aphrodite[5],raan=Aphrodite[3],arg_pe=Aphrodite[4],M0=Aphrodite[6],body=sun)
#orbit3 = KeplerianElements(a=Gaia[1],e=Gaia[2],i=Gaia[5],raan=Gaia[3],arg_pe=Gaia[4],M0=Gaia[6],body=sun)
#orbit4 = KeplerianElements(a=Ares[1],e=Ares[2],i=Ares[5],raan=Ares[3],arg_pe=Ares[4],M0=Ares[6],body=sun)
#orbit5 = KeplerianElements(a=Zeus[1],e=Zeus[2],i=Zeus[5],raan=Zeus[3],arg_pe=Zeus[4],M0=Zeus[6],body=sun)
#orbit6 = KeplerianElements(a=Cronus[1],e=Cronus[2],i=Cronus[5],raan=Cronus[3],arg_pe=Cronus[4],M0=Cronus[6],body=sun)
#orbit7 = KeplerianElements(a=Ouranos[1],e=Ouranos[2],i=Ouranos[5],raan=Ouranos[3],arg_pe=Ouranos[4],M0=Ouranos[6],body=sun)
#orbit8 = KeplerianElements(a=Poseiden[1],e=Poseiden[2],i=Poseiden[5],raan=Poseiden[3],arg_pe=Poseiden[4],M0=Poseiden[6],body=sun)