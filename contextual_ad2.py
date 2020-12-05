import cv2 
import time
import numpy as np

cap = cv2.VideoCapture('cadbury.mp4') 
print("Current Time is : " + str(time.time()))
start_time = time.time()

while(True): 
	
	# Capture frames in the video 
	ret, frame = cap.read() 

	font = cv2.FONT_HERSHEY_SIMPLEX 

	# inserting text on video 
	curr_time = time.time()
	if (curr_time > start_time + 10) and (curr_time < start_time + 14) :
		cv2.putText(frame, 'Show Jewellers Advertisement', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4) 
	if (curr_time > start_time + 21) and (curr_time < start_time + 25) :
		cv2.putText(frame, 'Show Optician Advertisement', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4) 
	if (curr_time > start_time + 31) and (curr_time < start_time + 35) :
		cv2.putText(frame, 'Show Selection Advertisement', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4) 				
	if (curr_time > start_time + 44) and (curr_time < start_time + 49) :
		cv2.putText(frame, 'Show Watches Advertisement', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4) 
	if (curr_time > start_time + 53) and (curr_time < start_time + 57) :
		cv2.putText(frame, 'Show Dryfruits Advertisement', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4) 

	# Display the resulting frame 
	cv2.imshow('video', frame) 

	# creating 'q' as the quit 
	# button for the video 
	if cv2.waitKey(30) & 0xFF == ord('q'): 
		break

# release the cap object 
cap.release() 
# close all windows 
cv2.destroyAllWindows() 
