from math import dist
dims=500
norm = dist([0,0],[dims/2,dims/2])**2/2

file = open("pic.ppm", 'w')
file.write('P3 ' + str(dims)+' '+str(dims)+' 255\n')
for i in range(int(dims)):
    for j in range(int(dims)):
        distance=dist([i,j],[dims/2,dims/2])**3
        distance/=norm
        distance%=1
        color=distance*255
        color=int(color)
        # invert
        icolor=255-color
        icolor=int(icolor)

        R=0
        G=icolor
        B=icolor
        file.write(str(R)+' '+str(G)+' '+str(B)+' ')

file.close()