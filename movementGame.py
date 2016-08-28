import pygame
import random
pygame.init()
# window setup
size=[400,300]
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()

# player position
x=size[0]/2
y=size[1]/2

# ball position
ballX=random.randrange(0,size[0])
ballY=random.randrange(0,size[1])

# colours
red=pygame.color.Color("#FF8080")
blue=pygame.color.Color("#8080FF")
white=pygame.color.Color("#FFFFFF")
black=pygame.color.Color("#000000")

def checkOffScreenX(x):
	if x>size[0]:
		x=0
	elif x<0:
		x=size[0]
	return x
def checkOffScreenY(y):
	if y>size[1]:
		y=0
	elif y<0:
		y=size[1]
	return y
def checkTouching():
	"""
	causes a mini explosion if the players are touching
	"""
	global x
	global ballX
	global y
	global ballY

	# check if player and ball are touching
	if -10<y-ballY<10 and -10<x-ballX<10:
		# draw an explosion
		pygame.draw.circle(screen,white,[x,y],15)

		xDiff=x-ballX
		yDiff=y-ballY

		# check if ball is on edge of screen
		if ballX==0:
			xDiff-=5
		elif ballX==size[0]:
			xDiff+=5
		if ballY==0:
			yDiff-=5
		elif ballY==size[1]:
			yDiff+=5

		# move the ball and player
		x+=xDiff*3
		ballX-=xDiff*3

		y+=yDiff*3
		ballY-=yDiff*3

# Game loop
done=False
while not done:
	screen.fill(black)

	keys=pygame.key.get_pressed()

	#player movement
	if keys[pygame.K_w]:
		y-=6
	if keys[pygame.K_s]:
		y+=6
	if keys[pygame.K_a]:
		x-=6
	if keys[pygame.K_d]:
		x+=6

	# check if player is touching the ball
	checkTouching()  
	#draw player
	pygame.draw.circle(screen,red,[x,y],6)
	#draw ball
	pygame.draw.circle(screen,blue,[ballX,ballY],6)

	pygame.display.flip()

	# ckeck off screen
	x=checkOffScreenX(x)
	y=checkOffScreenY(y)
	ballX=checkOffScreenX(ballX)
	ballY=checkOffScreenY(ballY)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	clock.tick(32)
pygame.quit()

