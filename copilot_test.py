import os
import platform
import time

def get_uptime():
    if platform.system() == "Windows":
        import ctypes
        from ctypes import wintypes, windll

        class Uptime(ctypes.Structure):
            _fields_ = [("IdleTime", wintypes.DWORD),
                        ("TickCount", wintypes.DWORD)]
        uptime = windll.kernel32.GetTickCount64() / 1000.0
        return uptime
    else:
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                return uptime_seconds
        except FileNotFoundError:
            # Fallback for systems without /proc/uptime
            return time.time() - psutil.boot_time()

def print_uptime():
    uptime_seconds = get_uptime()
    uptime_string = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
    print(f"System uptime: {uptime_string} (hh:mm:ss)")

if __name__ == "__main__":
    print_uptime()
