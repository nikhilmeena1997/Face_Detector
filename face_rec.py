import cv2
import numpy as np

cap=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

skip = 0
face_data = []
dataset_path = './Face_snaps/'
file_name = input("Enter Your Name please :")
while(True):
	ret,frame = cap.read()
	grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret == False:
		continue
		
	faces = face_cascade.detectMultiScale(grey_frame,1.3,5)
	faces = sorted(faces,key=lambda f:f[2]*f[3]) 
	 
	#picking the last face which is of largest area
	for (x,y,w,h) in faces[-1:]:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		
		#extract out the required face: Region of Interest..
		offset=10
		face_section = 	frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_section =  cv2.resize(face_section,(100,100))
		skip+=1
		if skip%10==0:
			face_data.append(face_section)
			print(len(face_data))  	
		cv2.imshow("face Section",face_section)
		if len(face_data)==10:
			break	

	cv2.imshow('Video Frame..',frame)
	
	#Keeping a track of exit condition..
	key_pressed=cv2.waitKey(1)&0xFF

	if key_pressed==ord('q'):
		break	
#Convert our face list into a numpy array..
face_data = np.asarray(face_data)
face_data=face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)


#save this data  into file system
np.save(dataset_path+file_name+'.npy',face_data)
print("Data Successfully Saved at"+dataset_path+file_name+'.npy')
cap.release()
cv2.destroyAllWindows()
