import os
import threading
import time

# Hàm để thực thi lệnh git push origin main
def push_to_main():
    countdown = 5 * 60  # 5 phút
    while True:
        os.system('git push origin main')
        print(f"Đang đợi {countdown // 60} phút {countdown % 60} giây cho lần push tiếp theo.")
        time.sleep(1)  # Đếm ngược
        countdown -= 1

# Tạo một luồng để chạy hàm push_to_main
thread = threading.Thread(target=push_to_main)
thread.start()

# Chờ luồng kết thúc (trong trường hợp này, mã này sẽ chạy vô hạn)
thread.join()
