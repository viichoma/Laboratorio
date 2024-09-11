
import cv2
import os

video_path = 'Dataset\Handgun\PAH2_C2_P3_V1_HB_4\PAH2_C2_P3_V1_HB_4.mp4'
output_folder = 'D:/Laboratorio/custom_dataset/dataset/train/images'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Abrir o vídeo
cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Salvar o frame como imagem
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f'Extraídos {frame_count} frames para {output_folder}')
