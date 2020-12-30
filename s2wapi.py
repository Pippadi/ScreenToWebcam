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
        return self._checkReturncode0(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'is-running'])
    
    def isInUse(self):
        return self._checkReturncode0(['/home/prithvi/Projects/ScreenToWebcam/ScreenToWebcam.sh', 'in-use'])
    
    def _checkReturncode0(self, cmd):
        runChecker = subprocess.Popen(cmd)
        runChecker.wait()
        return runChecker.returncode == 0