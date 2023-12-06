import argparse
import subprocess
import json
import tkinter as tk
import os
import random 
import string 

class CommunicationWrapper:
    def __init__(self, exe_name, target_exe):
        self.exe_name = exe_name
        self.target_exe = target_exe

    @staticmethod
    def generate_random_string(strlen=7):
        res = ''.join(random.choices(string.ascii_uppercase +
                                    string.digits, k=strlen))
        return str(res)
        
    def receive_message(self):
        return input()

    def send_message(self, message):
        print(json.dumps(message), flush=True)

    def alert(self, title, text):
        root = tk.Tk()
        root.geometry("600x250")
        root.eval('tk::PlaceWindow . center')
        root.title(title)
        label = tk.Label(root, text=text, font=("Helvetica", 14))
        label.pack(padx=10, pady=10)
        root.mainloop()

    def run(self, args):
        parser = argparse.ArgumentParser(description=f"{self.exe_name} Script")
        parser.add_argument("--message", type=str, help="Message to send")
        args = parser.parse_args(args)
       
        if not os.path.exists(self.target_exe):
            self.alert(title=f"{self.exe_name}", text=f"Error: Target executable '{self.target_exe}' not found. Exiting.")
            return
    
        if args.message:
            message_data = json.loads(args.message)
            communication_limit = message_data.get("communication_limit", 0)

        if communication_limit is None:
            self.alert(title=f"{self.exe_name}", text="Warning: Communication limit not provided. Exiting.")
            return

        if args.message:
            try:
                message_data = json.loads(args.message)
                counter = message_data.get("counter", 0)
            except json.JSONDecodeError:
                pass

        if counter >= communication_limit:
            self.alert(title=f"{self.exe_name}", text=f"Counter reached {communication_limit}. Exiting.")
            return

        counter += 1

        if args.message:
            received_message = json.loads(args.message).get("message", "")
            self.alert(title=f"{self.exe_name}", text=f"Received arg:\n{received_message}\nCounter: {counter}")

            received_message = json.loads(args.message).get("message", "")
            self.send_message({"message": received_message, "counter": counter})

            # Call the target_exe with the serialized message as an argument
            subprocess.run([self.target_exe, "--message", json.dumps({"message": received_message + "\n" + self.generate_random_string(), "counter": counter, "communication_limit": communication_limit})])
        else:
            self.alert(title=f"{self.exe_name}", text=f"No message provided. Counter: {counter}")
            # print(f"No message provided. Counter: {counter}")
