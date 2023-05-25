import subprocess
import netifaces
import psutil
from tkinter import *


def get_interface_list():
    interfaces = netifaces.interfaces()
    return interfaces


def get_network_interface_identifiers():
    interfaces = psutil.net_if_addrs()
    identifiers = []

    for interface_name, _ in interfaces.items():
        identifiers.append(interface_name)

    return identifiers


def get_ip_address():
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ipv4_addresses = addresses[netifaces.AF_INET]
            for entry in ipv4_addresses:
                ip_address = entry['addr']
                if ip_address != '127.0.0.1':
                    return ip_address

    return None


# 네트워크 인터페이스 식별자 가져오기
interface_identifiers = get_network_interface_identifiers()
interface_list = get_interface_list()

# IP 주소 가져오기
device_ip_address = get_ip_address()
device_network_interface = '\\Device\\NPF_' + str(interface_list[0])

cicflowmeter_cmd = 'cicflowmeter.exe -i ' + str(device_network_interface) + ' -c flows.csv -u http://localhost:5000//predict'

cicflowmeter_process = subprocess.run(cicflowmeter_cmd, shell=True)
# suricata_process = subprocess.run('python', shell=True)

# # subprocess 객체를 저장할 전역 변수
# cicflowmeter_process = None
# suricata_process = None
#
# def start_subprocess():
#     global cicflowmeter_process
#     global suricata_process
#
#     if cicflowmeter_process is None:
#         cicflowmeter_process = subprocess.run(cicflowmeter_cmd, shell=True)
#         suricata_process = subprocess.run('python', shell=True)
#
#         print("Subprocess Started.")
#
#
# def stop_subprocess():
#     global cicflowmeter_process
#     global suricata_process
#     if cicflowmeter_process is not None:
#         cicflowmeter_process.terminate()
#         suricata_process.terminate()
#         cicflowmeter_process = None
#         suricata_process = None
#         print("Subprocess Stoped.")
#
# # Tkinter 윈도우 생성
# window = Tk()
#
# # 시작 버튼 생성
# start_button = Button(window, text="Start", command=start_subprocess)
# start_button.pack()
#
# # 정지 버튼 생성
# stop_button = Button(window, text="Stop", command=stop_subprocess)
# stop_button.pack()
#
# # Tkinter 이벤트 루프 실행
# window.mainloop()




