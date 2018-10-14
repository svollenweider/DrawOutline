import numpy as np

a = np.array([[1,1,0],[2,0,0],[-1,1,0]])

def draw_outline(inputarray,Magnitude=1)
	Difference = a-np.roll(a,1,axis=0)
	Normals = np.cross(Difference,[0,0,-1])
	Normals = Normals/np.linalg.norm(Normals,axis=1)[:,None]

	Direction = np.zeros_like(Normals)
	for i in range(len(Normals)):
		k = (i+1)%len(Normals)
		Angle = np.arccos(np.dot(Normals[i],Normals[k]))/2
		Direction[i] = a[i] + Magnitude*(Normals[i]+Normals[k])/(2*(np.cos(Angle))**2)
	return Direction	
	