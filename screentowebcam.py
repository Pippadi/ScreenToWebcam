import subprocess, os, signal

class ScreenToWebcam:
    def start(self, height, width, mirror):
        subprocess.check_call(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'start', ("-m" if mirror else ""), '{}x{}'.format(height, width)])
    
    def stop(self):
        subprocess.run(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'stop'])

    def isRunning(self):
        runChecker = subprocess.Popen(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'is-running'])
        runChecker.wait()
        return runChecker.returncode == 0