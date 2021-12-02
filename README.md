# ScreenToWebcam
Grabs screen contents and sends to a virtual webcam.
## Requirements
- `ffmpeg`
- `v4l2loopback`
## Usage
Get the script by cloning this repo or [downloading the ZIP](https://github.com/Pippadi/ScreenToWebcam/archive/refs/heads/main.zip). Switch to Xorg/X11 if using Wayland. Run the script:
```
./ScreenToWebcam.sh [-m|--mirror] InputSize [OutputRes]
```
`InputSize` is the rectangle of pixels grabbed from the top-left corner of the screen, and `OutputRes` the resolution of the webcam feed. `--mirror` sets whether the webcam feed should be horizontally flipped. \
You will be prompted for your root password on start to initialize the v4l2loopback module, and on terminating to remove the module.
### Example
`./ScreenToWebcam.sh --mirror 1680x1050` grabs a 1680x1050 screen and creates a webcam feed. When `OutputRes` is omitted, it defaults to 1280x720.

---

Read more at the [Mysore LUG Website](https://mysorelug.indriyallc.net/articles/2021/11/screen-to-webcam/index.html).
