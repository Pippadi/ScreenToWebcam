import subprocess

class ScreenToWebcam:
    def start(self):
        self.s2wproc = subprocess.Popen('~/Projects/ScreenToWebcam/ScreenToWebcam.sh 1680x1050', shell=True)
    
    def stop(self):
        self.s2wproc.terminate()

    def isRunning(self):
        modSearch = subprocess.run("ps -ef | grep ScreenToWebcam.sh | grep -v grep", shell=True)
        return modSearch.returncode == 0