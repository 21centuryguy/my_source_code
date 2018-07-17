#Solar System 3D Animation using Glowscript - www.101computing.net/solar-system/

sun=sphere(color=vector(1,1,0),pos=vec(0,0,0),radius=1.5, shininess=10)
earth=sphere(color=vector(0,0,1),pos=vec(10,0,0),radius=1, shininess=10, make_trail=True)
moon=sphere(color=vector(0.5,0.5,0.5),pos=vec(12,0,0),radius=0.5, shininess=10, make_trail=True)

earth.make_trail=True
moon.make_trail=False

framerate=50
earthOmega=2*3.14159/365
moonAngle=0
moonOmega=2*3.14159/28

while True:
  rate(framerate)
  earth.rotate(angle=earthOmega, axis=vector(0,1,0), origin=vector(0,0,0))

  moonAngle+=moonOmega

  moon.pos=earth.pos + vector(2,0,0)
  moon.rotate(angle=moonAngle, axis=vector(0,1,0), origin=earth.pos)