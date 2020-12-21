#!/bin/bash

if [ -z $1 ] ; then
	echo "Usage: ./ScreenToWebcam  <InputSize> [OutputRes]
InputSize: Required field
           Size of the screen to be grabbed
OutputRes: Optional field
           Resolution the input will be scaled to in the output
           Defaults to 720 columns, preserving the aspect ratio of InputSize"
	exit 1
fi

outputRes=$( echo "$2" | sed -e s/x/:/ )
if [ -z $outputRes ] ; then
	outputRes="-1:720"
fi

sudo modprobe v4l2loopback devices=1 exclusive_caps=1 card_label=ScreenToWebcam video_nr=10
ffmpeg -f x11grab -video_size "$1" -i $DISPLAY -vf vflip -vf "scale=$outputRes,hflip,format=yuv420p" -c:a copy -f v4l2 /dev/video10
