
from ExeGenerator import ExeGenerator
import subprocess

def initiate_conversation(exe_name, arguments):
    exe_path = f"dist/{exe_name}.exe"  # Assuming the 'dist' directory contains the executables
    command = [exe_path] + arguments
    subprocess.run(command)

if __name__ == "__main__":
    exe_name = "Person"
    generator = ExeGenerator(base_name=exe_name, num_executables=6)
    generator.generate_and_cleanup()


    arguments = [
        "--message",
        "{\"message\": \"Let's Talk\", \"counter\": 0, \"communication_limit\": 10}"
    ]
    initiate_conversation(f"{exe_name}0", arguments)