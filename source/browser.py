import re

import requests
import xmltodict


class Browser:
    def __init__(self):
        self.url = 'http://192.168.8.1/'
        self.relogin()
        self._msgs = []

    def relogin(self):
        self.session = requests.Session()
        self.session.get(self.url + 'html/index.html')
        self.token_cash = self._get_csrf_token()[0]

    def _get_csrf_token(self):
        r = self.session.get(self.url + 'html/smsinbox.html').text
        p = re.compile("\"([A-Za-z0-9+=/]{32})\"")
        return re.findall(p, r)

    def _get_page(self, url):
        token = {'__RequestVerificationToken': self.token_cash}
        xml = self.session.get(url, headers=token).content
        return xmltodict.parse(xml) if xml else 'No response'

    def _post_page(self, url, data):
        token = {'__RequestVerificationToken': self.token_cash}
        xml = self.session.post(url, headers=token, data=data).content
        return xmltodict.parse(xml) if xml else 'No response'

    def get_sms(self, read_count='20'):
        if self._msgs:
            return self._msgs

        url = '{}api/sms/sms-list'.format(self.url)
        data = '<?xml version="1.0" encoding="UTF-8"?><request><PageIndex>1</PageIndex><ReadCount>{}</ReadCount>' \
               '<BoxType>1</BoxType><SortType>0</SortType><Ascending>0</Ascending><UnreadPreferred>0</UnreadPref' \
               'erred></request>'.format(read_count)

        msgs = self._post_page(url, data)
        if 'response' in msgs:
            self._msgs = self._parse(msgs)
            return self._msgs
        else:
            print('Bad response')

    def _is_new_msg(self):
        self.relogin()
        page = self._get_page(self.url + 'api/monitoring/check-notifications')
        if 'response' in page:
            if page['response']['UnreadMessage'] != '0':
                return True
        return False

    @staticmethod
    def _parse(data):
        msgs_list = []
        msgs = data['response']['Messages']['Message']
        for msg in msgs:
            msgs_list.append({
                'id': msg['Index'],
                'read': True if msg['Smstat'] == '1' else False,
                'sender': msg['Phone'],
                'msg': msg['Content'].replace('\n', ''),
                'date': msg['Date']
            })

        return msgs_list

    def get_new_sms(self):
        new_msgs = []
        if self._is_new_msg():
            msgs = self.get_sms()
            for msg in msgs:
                if not msg['read']:
                    new_msgs.append(msg)
        return new_msgs

    def set_read(self, index):
        self.relogin()
        url = self.url + 'api/sms/set-read'
        data = '<?xml version="1.0" encoding="UTF-8"?><request><Index>{}</Index></request>'.format(index)
        return self._post_page(url, data)

    def set_read_all(self):
        new_sms = self.get_new_sms()
        for msg in new_sms:
            self.set_read(msg['id'])


if __name__ == '__main__':
    pass
