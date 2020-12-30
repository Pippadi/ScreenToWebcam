import subprocess, os, signal

class ScreenToWebcam:
    def start(self, height, width, mirror):
        cmd = ['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'start', '{}x{}'.format(height, width)]
        if mirror:
            cmd.insert(2, "-m")
        subprocess.check_call(cmd)
    
    def stop(self):
        subprocess.run(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'stop'])

    def isRunning(self):
        runChecker = subprocess.Popen(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'is-running'])
        runChecker.wait()
        return runChecker.returncode == 0