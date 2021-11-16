#!/bin/bash

usage="Usage: ./ScreenToWebcam  [options] [values]
E.g. ./ScreenToWebcam --mirror 1680x1050 1920x1080

-m,--mirror: Flip webcam feed horizontally

-- Values --
InputSize:  Required field for start
            Size of the screen to be grabbed
            '1680x1050' in example given
OutputRes:  Optional field for start
            Resolution the input will be scaled to in the output
            Defaults to 1280x720"

startS2W () {
	if [ $XDG_SESSION_TYPE != "x11" ] ; then
		printf "\033[31mYou don't appear to be using X11!\033[37m\n"
		echo "Switch to X11/Xorg and try again."
		exit 1
	fi

	mirrorOpt=""
	if [ "$1" = "-m" ] || [ "$1" = "--mirror" ] ; then
		mirrorOpt="hflip,"
		shift
	fi

	if [ -z "$1" ] ; then
		echo "$usage"
		exit 1
	fi

	inputVals=(${1//+/ +})

	outputRes=$( echo "$2" | sed -e s/x/:/ )
	if [ -z $outputRes ] ; then
		outputRes="1280:720"
	fi

	printf "=========== Starting ScreenToWebcam ============\n"
	printf "============= Press Ctrl-C to exit =============\n\n"

	loopbackNum=0
	if find /dev | grep -q video ; then
		videoDevNums=($(find /dev/video* | sed -e 's|/dev/video||'))
		loopbackNum=$((${videoDevNums[*]: -1} + 1))
	fi
	pkexec /sbin/modprobe v4l2loopback devices=1 exclusive_caps=1 card_label=ScreenToWebcam video_nr=$loopbackNum
	ffmpegCmd="ffmpeg -f x11grab -video_size ${inputVals[0]} -i $DISPLAY${inputVals[1]} -vf scale=$outputRes,${mirrorOpt}format=yuv420p -r 15 -c:a copy -f v4l2 /dev/video$loopbackNum"
	printf "Starting ffmpeg.\n\n"
	$ffmpegCmd > /dev/null
}

inUse () {
	test "$(lsmod | grep -e ^v4l2loopback | awk '{print $3}')" -gt 0
}

stopS2W () {
	printf "\n\n========== Stopping ScreenToWebcam ==========\n"
	if ! inUse ; then
		pkexec /sbin/modprobe -r v4l2loopback
	else
		printf "\033[31mStill in use! Close programs using it and try again.\033[37m\n\n"
		while true ; do sleep 1 ; done
	fi
	exit $?
}

trap stopS2W SIGTERM
trap stopS2W SIGINT
startS2W $1 $2 $3
