import config
import os
import subprocess
p = subprocess.Popen(['./torrent_send.sh'])
sts = os.waitpid(p.pid, 0)
