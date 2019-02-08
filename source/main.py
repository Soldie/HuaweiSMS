import subprocess
import dump_to_file as file
import sender
import browser


class Main:
    def __init__(self):
        self.start()

    def is_WiFi(self):
        interface = subprocess.check_output('netsh wlan show interface', stdin=subprocess.PIPE,
                                            stderr=subprocess.PIPE).decode('cp866').strip()
        return 'MY Wi-Fi name' in interface

    def compare(self, data1, data2):
        for msg in data1:
            msg['read'] = True

        for msg in data2:
            msg['read'] = True

        return list(map(dict, set(tuple(x.items()) for x in data1 + data2)))

    def start(self):
        if self.is_WiFi():
            b = browser.Browser()
            new_sms = b.get_new_sms()

            if new_sms:
                s = sender.Sender()
                s.send(new_sms)

                b.set_read_all()

                data1 = b.get_sms()

                f = file.File()
                data2 = f.read()

                data = self.compare(data1, data2)
                f.write(data)


if __name__ == '__main__':
    m = Main()
