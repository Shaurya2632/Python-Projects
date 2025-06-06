import cv2
import numpy as np

# --------------------------- Basic Image I/O ---------------------------
img = cv2.imread('path/to/image.jpg', cv2.IMREAD_COLOR)   # Load image in color
cv2.imshow('Original Image', img)                         # Show image
cv2.waitKey(0)                                            # Wait for key press
cv2.destroyAllWindows()                                  # Close all OpenCV windows
cv2.imwrite('output.jpg', img)                           # Save image

# --------------------------- Image Properties ---------------------------
height, width, channels = img.shape                      # Dimensions and channels
size = img.size                                           # Total number of pixels
img_dtype = img.dtype                                     # Image data type

# --------------------------- Color Space Conversion ---------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

# --------------------------- Resize and Cropping ---------------------------
resized = cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA)
cropped = img[50:200, 100:300]                            # Crop region from y:50–200, x:100–300

# --------------------------- Overlay and Subtract Two Images ---------------------------
img2 = cv2.imread('path/to/another_image.jpg')
img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

# overlap
blended = cv2.addWeighted(img, 0.7, img2, 0.3, 0)

# subtract
sub = cv2.subtract(img, img2)

# --------------------------- Split and Merge Channels ---------------------------
b,g,r = cv2.split(img)                                    # Split BGR channels
merged = cv2.merge((b,g,r))                               # Merge BGR channels

# --------------------------- Image Thresholding ---------------------------
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
_, trunc = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
_, tozero = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)

# Adaptive Thresholding
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

# --------------------------- Blurring and Smoothing ---------------------------
gauss = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# --------------------------- Drawing Shapes & Text ---------------------------
draw_img = img.copy()
cv2.line(draw_img, (0,0), (100,100), (255,0,0), 3)
cv2.rectangle(draw_img, (50,50), (150,150), (0,255,0), 2)
cv2.circle(draw_img, (200,200), 50, (0,0,255), -1)
cv2.ellipse(draw_img, (300,300), (100,50), 0, 0, 180, (255,255,0), 2)
cv2.putText(draw_img, 'OpenCV', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2)

# --------------------------- ROI & Masking ---------------------------
roi = img[100:200, 100:200]
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (100,100), (200,200), 255, -1)
masked_img = cv2.bitwise_and(img, img, mask=mask)

# --------------------------- Bitwise Operations ---------------------------
bit_and = cv2.bitwise_and(img, img, mask=mask)
bit_or = cv2.bitwise_or(img, img, mask=mask)
bit_xor = cv2.bitwise_xor(img, img, mask=mask)
bit_not = cv2.bitwise_not(mask)

# --------------------------- Morphological Operations ---------------------------
kernel = np.ones((5,5), np.uint8)
dilate = cv2.dilate(binary, kernel, iterations=1)
erode = cv2.erode(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
grad = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

# --------------------------- Contours ---------------------------
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 2)

for c in contours:
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * perimeter, True)

# --------------------------- Geometric Transformations ---------------------------
rows, cols = img.shape[:2]
M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M_rotate, (cols, rows))

pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])
M_affine = cv2.getAffineTransform(pts1, pts2)
affine = cv2.warpAffine(img, M_affine, (cols, rows))

pts1_p = np.float32([[56,65], [368,52], [28,387], [389,390]])
pts2_p = np.float32([[0,0], [300,0], [0,300], [300,300]])
M_perspective = cv2.getPerspectiveTransform(pts1_p, pts2_p)
perspective = cv2.warpPerspective(img, M_perspective, (300, 300))

# --------------------------- Edge Detection ---------------------------
canny = cv2.Canny(gray, 100, 200)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# --------------------------- Corner Detection ---------------------------
gray_float = np.float32(gray)
dst = cv2.cornerHarris(gray_float, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
harris_img = img.copy()
harris_img[dst > 0.01 * dst.max()] = [0, 0, 255]

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.int0(corners)
corner_img = img.copy()
for i in corners:
    x,y = i.ravel()
    cv2.circle(corner_img, (x,y), 3, (0,255,0), -1)

# --------------------------- Feature Detection ---------------------------
sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(gray, None)
img_kp = cv2.drawKeypoints(img, kp, None)

# --------------------------- Mouse Events ---------------------------
mouse_img = img.copy()
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(mouse_img, (x,y), 10, (0,255,0), -1)
cv2.namedWindow('MouseEvent')
cv2.setMouseCallback('MouseEvent', draw_circle)
cv2.imshow('MouseEvent', mouse_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --------------------------- Video Capture ---------------------------
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# --------------------------- Haar Cascade Face Detection ---------------------------
face_img = img.copy()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(face_img, (x,y), (x+w, y+h), (255,0,0), 2)
cv2.imshow('Faces', face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()