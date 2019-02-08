# Huawei e3372h SMS

Forwards all new incoming messages SMS to the modem by email.

## Purpose

Redirection of all new messages to the email when the computer starts.

To read messages, you must go to **192.168.8.1** and open the list of messages. This is inconvenient, since it is possible in one day to forget to read the messages and go to the site, and there may be something important for you.

Therefore, I got the idea to make an automatic message analyzer.
The modem firmware provides an API set for working with it.

## Setup

* Set [here](https://github.com/kovinevmv/HuaweiSMS/blob/master/source/sender.py#L8) your gmail, password, and destination mail.
* Set [here](https://github.com/kovinevmv/HuaweiSMS/blob/master/source/main.py#L14) your Wi-Fi ESSID with Huawei e3372h
* Create executable file by pyinstaller:
```
pyinstaller --hidden-import=xmltodict main.py
```
* Add executable file to startup -> [Instruction](https://www.howtogeek.com/228467/how-to-make-a-program-run-at-startup-on-any-computer/)

## Example message

![Message](https://github.com/kovinevmv/HuaweiSMS/raw/master/docs/mail.png)

