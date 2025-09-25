# ลบ container ชื่อเดิมหากมี
docker rm -f opencv-app 2>/dev/null || true

# บิลด์ image (ที่โฟลเดอร์เดียวกับ Dockerfile/requirements.txt/app_cv.py)
docker build -t opencv-app .

# รัน โดยแมปโฟลเดอร์ output ออกมาดูไฟล์ได้
mkdir -p ./output
docker run -d --name opencv-app \
  -e OUTPUT_DIR=/data \
  -v "$(pwd)/output:/data" \
  opencv-app

# ดูสถานะ/ล็อก
docker ps -a
docker logs -f opencv-app

