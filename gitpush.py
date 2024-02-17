import os
import threading
import time

# Hàm để thực thi lệnh git push origin main
def push_to_main():
    while True:
        countdown = 2 * 60  # 5 phút
        while countdown > 0:
            mins, secs = divmod(countdown, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(f"Đợi {timeformat} trước khi thực hiện git push tiếp theo.")
            time.sleep(1)
            countdown -= 1

        os.system('git push origin main')
        print("Đã thực hiện git push.")

# Tạo một luồng để chạy hàm push_to_main
thread = threading.Thread(target=push_to_main)
thread.start()

# Chờ luồng kết thúc (trong trường hợp này, mã này sẽ chạy vô hạn)
thread.join()
