#import cv2
from imutils.video import VideoStream
import imutils
import time
import cv2

vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over frames
while True:
	# grab the next frame
	frame = vs.read()
	# resize the frame to have a maximum width of 500 pixels
	frame = imutils.resize(frame, width=500)
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# release the video stream and close open windows
vs.stop()
cv2.destroyAllWindows()