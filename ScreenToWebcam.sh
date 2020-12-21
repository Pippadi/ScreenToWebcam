sudo modprobe v4l2loopback devices=1 exclusive_caps=1 card_label=VirtCam video_nr=10
ffmpeg -f x11grab -video_size 1280x720 -i :1.0 -vf vflip -vf "hflip,format=yuv420p" -c:a copy -f v4l2 /dev/video10
