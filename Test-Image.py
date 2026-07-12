import cv2

img = cv2.imread("images/Happy.jpg")

if img is None:
    print("❌ Image not loaded")
else:
    print("✅ Image loaded successfully")
    cv2.imshow("Happy", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()