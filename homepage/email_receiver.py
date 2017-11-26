import os


class email_receiver():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "receiver_list.txt")
    email_list = []

    def __init__(self):
        for line in open(self.file_path, "r").readlines():
            self.email_list.append(line.strip())

    def add_new_receiver(self, email_address):
        self.email_list.append(email_address.strip())

    def remove_receiver(self, email_address):
        self.email_list.remove(email_address)

    def save_change(self):
        file = open(self.file_path, "w")
        print(self.email_list)
        for email in self.email_list:
            file.write(email + "\n")
        del self.email_list[:]

    def show_list(self):
        return email_list
