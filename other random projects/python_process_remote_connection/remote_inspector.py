# Note: Requires python 3.14+ and usually sudo

import sys

pid = int(sys.argv[1])
sys.remote_exec(pid, "inspector.py")
