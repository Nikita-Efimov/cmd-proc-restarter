from sys import argv
from time import sleep
import subprocess


def main():
    bashCommand = argv[1:]

    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, start_new_session=True)

    while True:
        if not process.poll() is None:
            process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, start_new_session=True)

        sleep(1)


if __name__ == "__main__":
    main()

