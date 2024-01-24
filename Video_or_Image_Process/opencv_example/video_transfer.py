import cv2
import time
import os
#cap=cv2.VideoCapture("udp://192.168.2.1:5000", cv2.CAP_FFMPEG)

file_list=os.listdir(os.path.abspath(os.getcwd()))
for i in range(len(file_list)):
	#print("{}: {}".format(i,file_list[i]))
	file_name=file_list[i]
	if file_name.find(".avi")!=-1:
		new_file_name=file_name.replace(".avi", "_fixed.mp4")
	elif file_name.find(".mp4")!=-1:
		new_file_name=file_name.replace(".mp4", "_fixed.mp4")
	else:
		continue
	print("{}. {} -> {}".format(i, file_name, new_file_name))
	cap=cv2.VideoCapture(file_name)
	#cap=cv2.VideoCapture("output.avi")
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	#fps = cap.get(cv2.CAP_PROP_FPS)
	fps=15

	size=(width, height)
	print("w: {}, h: {}, fps: {}".format(width, height, fps))
	#cap=cv2.VideoCapture("udpsrc host=192.168.2.4 port=5000 caps = \"application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96\" ! rtph264depay ! decodebin ! videoconvert ! appsink",cv2.CAP_GSTREAMER)
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(filename=new_file_name, apiPreference=cv2.CAP_ANY, fourcc=fourcc, fps=fps, frameSize=size)
	#fourcc = cv2.VideoWriter_fourcc(*'XVID')
	#out = cv2.VideoWriter(filename='output.avi',apiPreference=cv2.CAP_ANY ,fourcc=fourcc, fps=30, frameSize=size)

	start_time=time.time()
	ret, frame=cap.read()
	while ret:
		ret, frame=cap.read()

		if ret:
			'''
			with open("output.txt","a+") as f:
				now_time=time.time()
				f.write("{}\n".format(now_time-start_time))

				out.write(frame)
			'''
			out.write(frame)
			#cv2.imshow("webcam",frame)
		#if cv2.waitKey(32) & 0xFF == ord('q'):
			#break
	#cap.release()
	out.release()
	#cv2.destroyAllWindows()

