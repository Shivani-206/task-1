import platform
import subprocess
import time

def get_uptime():
    try:
        if platform.system() == "Windows":
            # Windows: use GetTickCount64 from ctypes
            import ctypes
            from ctypes import wintypes, windll

            uptime = windll.kernel32.GetTickCount64() / 1000.0
            return uptime
        elif platform.system() == "Linux":
            # Linux: read /proc/uptime
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                return uptime_seconds
        elif platform.system() == "Darwin":
            # macOS: use sysctl via subprocess
            result = subprocess.run(
                ["sysctl", "-n", "kern.boottime"],
                capture_output=True, text=True, check=True
            )
            boot_time_str = result.stdout.strip().split('=')[1].split(',')[0].strip()
            boot_time = int(boot_time_str)
            uptime_seconds = time.time() - boot_time
            return uptime_seconds
        else:
            raise NotImplementedError("Unsupported operating system.")
    except Exception as e:
        print(f"Error getting uptime: {e}")
        return None

def print_uptime():
    uptime_seconds = get_uptime()
    if uptime_seconds is not None:
        uptime_string = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
        print(f"System uptime: {uptime_string} (hh:mm:ss)")
    else:
        print("Could not determine system uptime.")

if __name__ == "__main__":
    print_uptime()
