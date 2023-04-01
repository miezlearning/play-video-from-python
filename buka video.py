import cv2
import pygame

# Buka file video
cap = cv2.VideoCapture('C:/Users/Administrator/Downloads/Video/Saikyou Onmyouji No Isekai Tenseiki S01E11.mp4')

# Dapatkan resolusi frame video asli
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Hitung aspek rasio dari video asli
aspect_ratio = width / height

# Atur lebar tampilan video menjadi 640 piksel dan tinggi disesuaikan dengan aspek rasio
display_width = 640
display_height = int(display_width / aspect_ratio)

# Dapatkan informasi framerate dari video
video_fps = cap.get(cv2.CAP_PROP_FPS)

# Set parameter-pre
frequency = 10000
size = -16
channels = 1
buffer = 324233

# Atur parameter-pre menggunakan pygame.mixer.pre_init()
pygame.mixer.pre_init(frequency, size, channels, buffer)

# Inisialisasi Pygame
pygame.init()

# Buka file audio
pygame.mixer.music.load('C:/Users/Administrator/Downloads/Music/percobaan.mp3')

# Putar audio
pygame.mixer.music.play()

# Looping melalui setiap frame video
clock = pygame.time.Clock()
while cap.isOpened():
    # Baca frame video
    ret, frame = cap.read()

    if ret:
        # Resize frame video ke ukuran tampilan
        resized_frame = cv2.resize(frame, (display_width, display_height))

        # Tampilkan frame video
        cv2.imshow('Video', resized_frame)

        # Sinkronisasi framerate video dan Pygame
        clock.tick(video_fps)

        # Hentikan video jika tombol 'q' ditekan
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Tutup file video dan jendela tampilan
cap.release()
cv2.destroyAllWindows()

# Hentikan audio setelah video selesai diputar
pygame.mixer.music.stop()
