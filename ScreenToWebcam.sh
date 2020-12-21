#!/bin/bash

if [ -z $1 ] ; then
	echo "Usage: ./ScreenToWebcam  <InputSize> [OutputRes]
InputSize: Required field
           Size of the screen to be grabbed
OutputRes: Optional field
           Resolution the input will be scaled to in the output
           Defaults to 1280x720"
	exit 1
fi

outputRes=$( echo "$2" | sed -e s/x/:/ )
if [ -z $outputRes ] ; then
	outputRes="1280:720"
fi

echo "Using output resolution $outputRes"
sudo modprobe v4l2loopback devices=1 exclusive_caps=1 card_label=VirtCam video_nr=10
ffmpeg -f x11grab -video_size "$1" -i :1.0 -vf vflip -vf "scale=$outputRes,hflip,format=yuv420p" -c:a copy -f v4l2 /dev/video10
