# ScreenToWebcam
Grabs screen contents and sends to a virtual webcam.
## Requirements
- `ffmpeg`
- `v4l2loopback`
- Python 3
- `PyGObject`
## Installation
- Download the Debian package from the 'Releases' section of this page.
- Navigate to the folder the package downloaded to, and install with `sudo apt install ./ScreenToWebcam.noarch.deb`.
## Usage
- Run script \
`ScreenToWebcam <command> [options]` \
`ScreenToWebcam start [-m|--mirror] InputSize [OutputRes]` \
Where `InputSize` is the rectangle of pixels grabbed from the top-left corner of the screen, and `OutputRes` the resolution of the webcam feed. `--mirror` sets whether the webcam feed should be horizontally flipped.
- Or just run the basic GUI.
### Examples
`ScreenToWebcam start --mirror 1680x1050` grabs a 1680x1050 screen and creates a webcam feed. When `OutputRes` is omitted, it defaults to 1280x720. \
`ScreenToWebcam stop` stops ScreenToWebcam if running.
## Removal
Run `sudo apt remove screentowebcam`.
