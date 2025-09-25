FROM python:3.9-slim

WORKDIR /app

# ติดตั้ง dependencies สำหรับ OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# คัดลอกและติดตั้ง Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์โปรเจกต์ทั้งหมด
COPY . .

# ตั้งค่า ENV ก่อน mkdir
ENV OUTPUT_DIR=/output
RUN mkdir -p ${OUTPUT_DIR}

# คำสั่งรันโปรเจกต์
CMD ["python", "app_cv.py"]
