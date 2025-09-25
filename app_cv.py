import cv2
import numpy as np
import time
import os
import math

# OUTPUT_DIR จาก environment variable
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ขนาดภาพ
height, width = 480, 640
center = (width // 2, height // 2)
radius = 150

# คำนวณจุด 5 แฉกของดาว
def get_star_points(center, radius):
    cx, cy = center
    points = []
    for i in range(5):
        angle_deg = 72 * i - 90  # เริ่มจากบนสุด
        angle_rad = math.radians(angle_deg)
        x = int(cx + radius * math.cos(angle_rad))
        y = int(cy + radius * math.sin(angle_rad))
        points.append((x, y))
    return points

# เชื่อมเส้นตามลำดับของดาว
star_order = [0, 2, 4, 1, 3, 0]

points = get_star_points(center, radius)

try:
    idx = 1
    while True:
        # สร้างภาพใหม่
        img = 255 * np.ones((height, width, 3), dtype="uint8")

        # วาดเส้นทีละเส้น (จากลำดับ star_order)
        for i in range(1, idx):
            pt1 = points[star_order[i - 1]]
            pt2 = points[star_order[i]]
            cv2.line(img, pt1, pt2, (0, 0, 255), 2)

        # เซฟภาพ
        filepath = os.path.join(OUTPUT_DIR, "updated.jpg")
        cv2.imwrite(filepath, img)
        print(f"Saved: {filepath}")

        # เพิ่มจำนวนเส้น
        idx += 1
        if idx > len(star_order):
            idx = 1  # เริ่มใหม่

        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")
