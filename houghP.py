import time
import cv2
import numpy as np

cap = cv2.VideoCapture("0degree.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while(True):
	ret, frame = cap.read()

	ysize = frame.shape[0]
	xsize = frame.shape[1]


	left = frame[0:ysize, 0:int(xsize/2)]
	right = frame[0:ysize, int(xsize/2):xsize]

	grayright = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
	grayleft = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)

	edgesl = cv2.Canny(grayleft,75,100,apertureSize = 3)
	edgesr = cv2.Canny(grayright,75,100,apertureSize = 3)
	minLineLength = 1000
	maxLineGap = 1
	linesl = cv2.HoughLinesP(edgesl,35,np.pi/180,150,minLineLength,maxLineGap)
	linesr = cv2.HoughLinesP(edgesr,35,np.pi/180,150,minLineLength,maxLineGap)

	if linesr != None:
		for i in range(0,len(linesr)):
			for x1,y1,x2,y2 in linesr[i]:

				cv2.line(right,(x1,y1),(x2,y2),(0,255,0),5,8)

	if linesl != None:
		for k in range(0,len(linesl)):
			for x1,y1,x2,y2 in linesl[k]:

				cv2.line(left,(x1,y1),(x2,y2),(0,255,0),5,8)
	
	#cv2.imshow('cannyl',edgesl)
	#cv2.imshow('cannyr',edgesr)
	cv2.imshow('left', left)
	cv2.imshow('right', right)


	# show the frame
	#cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF



	# clear the stream in preparation for the next frame
	#rawCapture.truncate(0)

	#if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cap.release()