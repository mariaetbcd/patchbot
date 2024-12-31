import os
import subprocess

class PatchBot:
    def __init__(self):
        self.installed_softwares = self.get_installed_softwares()

    @staticmethod
    def get_installed_softwares():
        software_list = []
        # This part of the code needs to be changed according to the platform
        # Below is an example for Ubuntu
        result = subprocess.run(['apt', 'list', '--installed'], stdout=subprocess.PIPE)
        installed = result.stdout.decode('utf-8').split('\n')
        for software in installed:
            software_list.append(software.split('/')[0])
        return software_list

    def check_updates(self):
        for software in self.installed_softwares:
            # This part of the code needs to be changed according to the platform
            # Below is an example for Ubuntu
            update_check = subprocess.run(['apt', 'list', software], stdout=subprocess.PIPE)
            if '[upgradable]' in update_check.stdout.decode('utf-8'):
                self.update_software(software)

    @staticmethod
    def update_software(software):
        # This part of the code needs to be changed according to the platform
        # Below is an example for Ubuntu
        subprocess.run(['apt-get', 'install', '--only-upgrade', '-y', software])

if __name__ == "__main__":
    bot = PatchBot()
    bot.check_updates()