import subprocess, os, signal

class ScreenToWebcam:
    def start(self, height, width):
        subprocess.check_call(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'start', '{}x{}'.format(height, width)])
    
    def stop(self):
        subprocess.run(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'stop'])

    def isRunning(self):
        runChecker = subprocess.Popen(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'is-running'])
        runChecker.wait()
        return runChecker.returncode == 0