# ScreenToWebcam
Grabs screen contents and sends to a virtual webcam.
## Requirements
- `ffmpeg` \
Install with `sudo apt install ffmpeg`
- `v4l2loopback` \
Install with `sudo apt install v4l2loopback-dkms`
## Usage
- Make script executable \
`chmod +x ScreenToWebcam.sh`
- Run script \
`./ScreenToWebcam.sh <command> [options]` \
`./ScreenToWebcam.sh start InputSize OutputRes` \
Where `InputSize` is the rectangle of pixels grabbed from the top-left corner of the screen, and `OutputRes` the resolution of the webcam feed
### Examples
`./ScreenToWebcam.sh start 1680x1050` grabs a 1680x1050 screen and creates a webcam feed. When `OutputRes` is omitted, it defaults to a 720-column resolution that preserves the aspect ratio of the input (in this case 16:10). \
`./ScreenToWebcam.sh stop` stops ScreenToWebcam if running.