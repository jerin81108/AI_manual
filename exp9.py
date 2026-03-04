import cv2, pyautogui, math, os, urllib.request
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Download model if not exists
model_path = "hand_landmarker.task"
if not os.path.exists(model_path):
    print("Downloading Mediapipe Hand Model...")
    urllib.request.urlretrieve("https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task", model_path)

# Initialize Hand Landmarker
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
pyautogui.FAILSAFE = False
sw, sh = pyautogui.size()
print("Virtual Mouse Activated. Press 'ESC' to exit.")

while cap.isOpened():
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1)
    ih, iw, _ = img.shape
    
    # Process with Tasks API
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    res = detector.detect(mp_image)
    
    if res.hand_landmarks:
        hand = res.hand_landmarks[0]
        
        # Get coordinates for Index (8) and Thumb (4) tips
        ix, iy = int(hand[8].x * iw), int(hand[8].y * ih)
        tx, ty = int(hand[4].x * iw), int(hand[4].y * ih)
        
        sx, sy = int(hand[8].x * sw), int(hand[8].y * sh)
        
        # Click if index and thumb are close
        if math.hypot(ix - tx, iy - ty) < 40:
            pyautogui.click()
            cv2.circle(img, (ix, iy), 15, (0, 255, 0), -1)
        else:
            pyautogui.moveTo(sx, sy)
            cv2.circle(img, (ix, iy), 15, (255, 0, 0), -1)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) == 27: break

cap.release()
cv2.destroyAllWindows()