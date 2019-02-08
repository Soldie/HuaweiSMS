import base64
import json


class File:
    def __init__(self):
        self.file_name = 'log.txt'

    def read(self):
        with open(self.file_name, 'r') as f:
            d = self._decode(f.read())
            file_data = json.loads(d)
            return file_data

    def write(self, data):
        json_data = json.dumps(data).encode()
        with open(self.file_name, 'w+') as f:
            f.write(self._encode(json_data))

    @staticmethod
    def _encode(data):
        return base64.b64encode(data).decode()

    @staticmethod
    def _decode(data):
        return base64.b64decode(data).decode()


if __name__ == '__main__':
    pass
