import datetime
import os
import random
import threading

def commit_changes(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        for i in range(random.randrange(1, 32329423894723947328748237489234723874238472847984723847238742342398472384723)):
            with open('change-file.txt', 'a') as wf:
                wf.write(f'\n{current_date}')
            os.system(f'git add .')
            os.system(f'git commit --date "{current_date}" -m "#{i} commit for {current_date}"')
        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    today = datetime.date.today()

    current_year = today.year
    current_month = today.month
    current_day = today.day

    last_year = current_year - 0
    last_month = today.month
    last_day = current_day - 0  # In case it is a leap year

    start_date = datetime.date(last_year, last_month, last_day)
    end_date = datetime.date(current_year, current_month, current_day)

    num_threads = 5  # You can adjust the number of threads based on your machine's capabilities
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=commit_changes, args=(start_date, end_date))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
