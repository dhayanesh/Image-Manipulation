import cv2

# Load two consecutive frames
frame1 = cv2.imread('frame1.png')
frame2 = cv2.imread('frame2.png')

# Convert frames to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

# Define the window size and max iterations for Lucas-Kanade
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Compute optical flow using Lucas-Kanade method
flow = cv2.calcOpticalFlowPyrLK(gray1, gray2, None, None, **lk_params)

# Separate the x and y components of the flow vectors
flow_x = flow[:, :, 0]
flow_y = flow[:, :, 1]

# Display the optical flow vectors
plt.quiver(flow_x, flow_y)
plt.show()
