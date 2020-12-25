import subprocess, os, signal

class ScreenToWebcam:
    def start(self):
        if not self.isRunning():
            subprocess.check_call(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'start', '1680x1050'])
        else:
            print("Already running. Doing nothing.")
    
    def stop(self):
        if self.isRunning():
            subprocess.check_call(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'stop'])
        else:
            print("Nothing to stop. Doing nothing.")

    def isRunning(self):
        running = subprocess.run(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'is-running'])
        return running.returncode == 0