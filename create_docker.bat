docker build -t opencv-docker .
docker run -d --name opencv-docker \
  -e OUTPUT_DIR=/data \
  -v "$(pwd)/output:/data" \
  opencv-docker