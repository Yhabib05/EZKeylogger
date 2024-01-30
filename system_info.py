#system_info.py
import socket
import platform
import psutil
import pyperclip


def get_system_info():
    with open("machine_infos.txt", 'w') as f:  # Open in write mode to create a new file or overwrite an existing one
        hostname= socket.gethostname()
        processor= platform.processor()
        platform_infos= platform.platform()
        os_name=platform.system()
        version= platform.version()
        #ip_adress= get_ip_adress()

        #writing system infos to the file
        f.write("=" * 60 + "\n")
        f.write("SYS INFOS".center(60) + "\n")
        f.write("=" * 60 + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Processor: " + processor + "\n")
        f.write("os name: " + os_name + "\n")
        f.write("os version and last update: " + version + "\n")
        f.write("More infos: "+ platform_infos + "\n")

def get_memory_info():
    with open("machine_infos.txt", 'a') as f: # Open in append mode to add to the existing file ;)
        f.write("=" * 60 + "\n")
        f.write("MEMORY INFOS".center(60) + "\n")
        f.write("=" * 60 + "\n")       
        total_memory =psutil.virtual_memory().total/(1024**3)
        used_memory = psutil.virtual_memory().used/(1024**3)
        available_memory = psutil.virtual_memory().available/(1024**3)
        percent_memory = psutil.virtual_memory().percent
       
        f.write("total memory: " + str(round(total_memory,2)) + "GB\n")
        f.write("used memory: " + str(round(used_memory,2)) + "GB\n")
        f.write("available memory: " + str(round(available_memory,2)) + "GB\n")
        f.write("percent memory: " + str(round(percent_memory,2)) + "GB\n")

def get_cpu_info():
    with open("machine_infos.txt", 'a') as f: 
        f.write("=" * 60 + "\n")
        f.write("CPU INFOS".center(60) + "\n")
        f.write("=" * 60 + "\n")       
        f.write("total CPU usage: " + str(psutil.cpu_percent(interval=1)) + "%\n")

## Needs xclip to be installed to work on linux!!!!!!!!!! (see documentation)
def get_clipboard_info():
    try:
        clipboard_content = pyperclip.paste()
    except pyperclip.PyperclipException:
        clipboard_content = "Clipboard content could not be retrieved."

    with open("machine_infos.txt", 'a') as f:
        f.write("=" * 60 + "\n")
        f.write("CLIPBOARD INFOS".center(60) + "\n")
        f.write("=" * 60 + "\n")
        f.write("Clipboard content: " + clipboard_content + "\n")




def gather_all_system_info():
    get_system_info()
    get_memory_info()
    get_cpu_info()
    get_clipboard_info()
