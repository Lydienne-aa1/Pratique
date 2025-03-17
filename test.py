import platform
import psutil


uname_result = platform.uname()

print(uname_result)
print(psutil.virtual_memory())