import os
import threading
import uuid
import time

def create_and_push_directory():
    parent_directory = '/Users/aedotris/Downloads/a'
    directory_name = str(uuid.uuid4())[:8]
    try:
        os.makedirs(os.path.join(parent_directory, directory_name))
        with open(os.path.join(parent_directory, directory_name, "file.txt"), "w") as f:
            f.write("khangne")
    except FileExistsError:
        pass

    time.sleep(0.2)

    # Push changes to Git
    os.chdir(parent_directory)
    os.system("git add .")
    os.system('git commit -m "Auto commit: added directory and file"')
    os.system("git push origin master")

def create_and_push_directories():
    while True:
        threads = []
        for _ in range(50):
            thread = threading.Thread(target=create_and_push_directory)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    create_and_push_directories()
