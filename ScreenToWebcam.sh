#!/bin/bash

usage="Usage: ./ScreenToWebcam  <command> [options] [values]
E.g. ./ScreenToWebcam start 1680x1050 1920x1080

start:      Starts ScreenToWebcam
stop:       Stops ScreenToWebcam
is-running: Checks whether ScreenToWebcam is running or not.
            Returns code 0 if running, else 1.

InputSize:  Required field for start
            Size of the screen to be grabbed
            '1680x1050' in example given
OutputRes:  Optional field for start
            Resolution the input will be scaled to in the output
            Defaults to 720 columns, preserving the aspect ratio of InputSize
            1920x1080 in example given"

ffmpegpidfile="/tmp/s2wffmpegpid"

startS2W () {
	mirrorOpt=""
	if [ "$1" = "-m" ] || [ "$1" = "--mirror" ] ; then
		mirrorOpt="hflip,"
		shift
	fi

	if [ -z $1 ] ; then
		echo "$usage"
		exit 1
	fi

	outputRes=$( echo "$2" | sed -e s/x/:/ )
	if [ -z $outputRes ] ; then
		outputRes="-1:720"
	fi

	echo "Starting ScreenToWebcam"

	videoDevNums=($(find /dev/video* | sed -e "s|/dev/video||"))
	loopbackNum=$((${videoDevNums[-1]} + 1))
	pkexec /sbin/modprobe v4l2loopback devices=1 exclusive_caps=1 card_label=ScreenToWebcam video_nr=$loopbackNum
	ffmpegCmd="ffmpeg -f x11grab -video_size $1 -i $DISPLAY -vf scale=$outputRes,${mirrorOpt}format=yuv420p -r 15 -c:a copy -f v4l2 /dev/video$loopbackNum"
	$ffmpegCmd &> /dev/null &
	echo $! > $ffmpegpidfile
}

stopS2W () {
	echo "Stopping ScreenToWebcam."
	if (xargs ps < $ffmpegpidfile) > /dev/null ; then
		xargs kill -s SIGTERM < $ffmpegpidfile
		tail --pid=$(cat $ffmpegpidfile) -f /dev/null
	fi
	pkexec /sbin/modprobe -r v4l2loopback
	modprobeExitCode=$?
	if [ $modprobeExitCode -eq 0 ] ; then
		rm $ffmpegpidfile
	fi
	exit $modprobeExitCode
}

isRunning () {
	test -f $ffmpegpidfile && test -n $ffmpegpidfile
}

inUse () {
	test "$(lsmod | grep -e ^v4l2loopback | awk '{print $3}')" -ne 1
}

case $1 in
	"start")
		if ! isRunning ; then
			startS2W "$2" "$3" "$4"
		else
			echo "ScreenToWebcam already running. Doing nothing."
		fi
	;;
	"stop")
		if isRunning ; then
			stopS2W
		else
			echo "ScreenToWebcam not running. Doing nothing."
		fi
	;;
	"is-running")
		isRunning
		exit $?
	;;
	"in-use")
		inUse
		exit $?
	;;
	*)
		echo "$usage"
		exit 1
	;;
esac
