import os
import shutil
import time

days = 30
path = input('Enter The Path : ')
path = path.replace('\\', '/')
path = path + '/'
files = os.listdir(path)
seconds = time.time() - days * 24 * 60 * 60


def removeFiles(lpath):
    if not os.remove(lpath):
        print(f'{lpath} Removed Succesfully')


def main():
    if os.path.exists(path):
        for root, folders, files in os.walk(path):
            for file in files:
                filePath = os.path.join(root, file)
                if os.stat(filePath).st_ctime <= seconds:
                    removeFiles(filePath)
    else:
        print('Path Not Found!')


if __name__ == "__main__":
    main()
