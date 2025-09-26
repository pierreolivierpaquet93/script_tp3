import time
import os
import random

class Tester:
    def __init__(self):
        self.start_timer = time.time()
        self.__file_1_path = None
        self.__file_2_path = None
        self.__file_3_path = None
        self.__secret_1 = f"A-{random.randint(0,99999)}"
        self.__secret_2 = f"B-{random.randint(0,99999)}"
        self.__secret_3 = f"C-{random.randint(0,99999)}"

    def prepare_secret_1(self, file_path):
        self.__file_1_path = file_path
        time.sleep(3.0)
        with open(self.__file_1_path, 'w', newline='') as file:
            file.write(self.__secret_1)

    def prepare_secret_2(self, file_path):
        self.__file_2_path = file_path
        time.sleep(1.0)
        with open(self.__file_2_path, 'w', newline='') as file:
            file.write(self.__secret_2)

    def prepare_secret_3(self, file_path):
        self.__file_3_path = file_path
        time.sleep(2.0)
        with open(self.__file_3_path, 'w', newline='') as file:
            file.write(self.__secret_3)

    def check_secrets(self, secret_1, secret_2, secret_3):
        end_time = time.time()
        valid = True
        for file in [self.__file_1_path, self.__file_2_path, self.__file_3_path]:
            if not file is None:
                if os.path.exists(file):
                    os.remove(file)

        if(self.__secret_1 == secret_1):
            print("You got the correct secret #1")
        else:
            print(f"You didn't get the correct secret #1...Expected={self.__secret_1} Received={secret_1}")
            valid = False
        if (self.__secret_2 == secret_2):
            print("You got the correct secret #2")
        else:
            print(f"You didn't get the correct secret #2...Expected={self.__secret_2} Received={secret_2}")
            valid = False
        if (self.__secret_3 == secret_3):
            print("You got the correct secret #3")
        else:
            print(f"You didn't get the correct secret #3...Expected={self.__secret_3} Received={secret_3}")
            valid = False
        duration = end_time - self.start_timer
        if duration <= 3.5:
            print("You were fast enough!")
        else:
            print(f"You didn't make it fast enough... Your test duration : {round(duration,1)} seconds, expected maximum 3.5 seconds")
            valid = False

        if valid:
            print("You pass the test!")
            return True

        print("You FAILED the test...")
        return False
