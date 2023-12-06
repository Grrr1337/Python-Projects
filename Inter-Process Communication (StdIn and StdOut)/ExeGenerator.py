import os
import subprocess
"""
Specifically designed for the CommunicationWrapper in order to temporarily create and build the executable files.
"""
class ExeGenerator:
    def __init__(self, base_name, num_executables):
        self.base_name = base_name
        self.num_executables = num_executables

    def generate_executables(self):
        for i in range(self.num_executables):
            with open(f"{self.base_name}{i}.py", "w") as file:
                file.write("from communication_wrapper import CommunicationWrapper\n")
                file.write("import sys\n")
                file.write(f"if __name__ == \"__main__\":\n")
                file.write(f"    wrapper = CommunicationWrapper(exe_name='{self.base_name}{i}', target_exe='{self.base_name}{(i+1)%self.num_executables}.exe')\n")
                file.write("    wrapper.run(sys.argv[1:])\n")

    def cleanup_temp_files(self):
        for i in range(self.num_executables):
            os.remove(f"{self.base_name}{i}.py")
            os.remove(f"{self.base_name}{i}.spec")

    def generate_and_cleanup(self):
        self.generate_executables()

        for i in range(self.num_executables):
            subprocess.run([
                "pyinstaller",
                "--onefile",
                "--noconsole",
                f"--name={self.base_name}{i}",
                f"{self.base_name}{i}.py"
            ])

        self.cleanup_temp_files()

