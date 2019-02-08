import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Sender:
    def __init__(self):
        self.source_email = 'source_mail@gmail.com'
        self.source_pass = 'pass'
        self.dest_email = 'dest_mail@gmail.com'


    def send(self, data):
        if data:
            text = self.data_to_text(data)

            msg = MIMEMultipart()
            msg['From'] = self.source_email
            msg['To'] = self.dest_email
            msg['Subject'] = 'Modem SMS: MYPHONE number'

            msg.attach(MIMEText(text, 'html'))
            try:
                mailServer = smtplib.SMTP("smtp.gmail.com", 587)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.login(self.source_email, self.source_pass)
                mailServer.sendmail(self.source_email, self.dest_email, msg.as_string())
                mailServer.close()
            except:
                pass

    def data_to_text(self, data):
        text = '<div data-marker="wrapper" style="" class="stylingblock-content-wrapper"></div><!DOCTYPE html' \
               'PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"><html xmlns="http://www.w3.org/TR/xhtml1/DTD/' \
               'xhtml1-transitional.dtd"> <head> <meta name="format-detection" content="telephone=no"> <meta ' \
               'name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scal' \
               'able=0"/> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> <title></titl' \
               'e> <link href=\'https://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic\' r' \
               'el=\'stylesheet\' type=\'text/css\'> <style type="text/css"> p{margin: 1em 0;}table td{borde' \
               'r-collapse: collapse;}img, a img{border: 0; height: auto; outline: none; text-decoration: no' \
               'ne;}@-ms-viewport{width: device-width;}h1, h2, h3, h4, h5, h6{display: block !important; mar' \
               'gin: 0 !important; padding: 0 !important;}body,{height: 100% !important; -webkit-text-size-a' \
               'djust: 100%; -ms-text-size-adjust: 100 margin: 0; padding: 0; width: 100% !important;}linkfi' \
               'x a{color: #bababa !important; text-decoration: none;}img{-ms-interpolation-mode: bicubic;}t' \
               'able{mso-table-lspace: 0pt; mso-table-rspace: 0pt;}.ReadMsgBody{width: 100%;}.ExternalClass{' \
               'width: 100%;}p, a, li, td, blockquote{mso-line-height-rule: exactly;}a[href^="tel"], a[href^' \
               '="sms"]{color: inherit; cursor: default; text-decoration: none;}p, a, li, td, body, table, b' \
               'lockquote{-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;}.ExternalClass, .Exter' \
               'nalClass p, .ExternalClass td, .ExternalClass div, .ExternalClass span, .ExternalClass font{' \
               'line-height: 100%;}body{width: 100%; background-color: #e8e8e8; margin: 0 auto; padding: 0; ' \
               '-webkit-font-smoothing: antialiased; font-family: "Arial", sans-serif !important;}@media onl' \
               'y screen and (max-device-width: 480px), screen and (max-width: 480px){body[yahoo]{width: 100' \
               '% !important; min-width: 100% !important; margin: 0 auto !important;}body[yahoo] .container{' \
               'width: 100% !important; max-width: 480px !important;}body[yahoo] .mobileShow{display: block ' \
               '!important; margin: 0 !important; padding: 0 !important; overflow: visible !important; width' \
               ': auto !important; max-height: inherit !important;}body[yahoo] .mobileHide{display: none !imp' \
               'ortant;}body[yahoo] .photo img{width: 100% !important; max-width: 100% !important; height: aut' \
               'o !important;}body[yahoo] .columnStack{width: 100% !important; display: block !important;}body' \
               '[yahoo] .contentCenter, body[yahoo] .contentCenter img, body[yahoo] .contentCenter table{margi' \
               'n: 0 auto !important;}body[yahoo] .textCenter{text-align: center !important;}body[yahoo] .text' \
               'Left{text-align: left !important;}body[yahoo] .nullBorder{border: none !important;}body[yahoo]' \
               '.alignTop{vertical-align: top !important;}body[yahoo] .autoHeight{height: auto !important;}/**' \
               '* PADDING ***/ body[yahoo] .nullPad{padding: 0px !important;}body[yahoo] .mobilePad{padding-ri' \
               'ght: 30px !important; padding-left: 30px !important;}body[yahoo] .bottomPad5{padding-bottom: 5' \
               'px !important;}body[yahoo] .topPad5{padding-bottom: 5px !important;}body[yahoo] .topPad10{padd' \
               'ing-top: 10px !important;}body[yahoo] .bottomPad10{padding-bottom: 10px !important;}body[yahoo' \
               '] .topPad15{padding-top: 15px !important;}body[yahoo] .bottomPad15{padding-bottom: 15px !impor' \
               'tant;}body[yahoo] .topPad20{padding-top: 20px !important;}body[yahoo] .bottomPad20{padding-bot' \
               'tom: 20px !important;}body[yahoo] .topPad25{padding-top: 25px !important;}body[yahoo] .bottomP' \
               'ad25{padding-bottom: 25px !important;}body[yahoo] .bottomPad30{padding-bottom: 30px !important' \
               ';}body[yahoo] .rightPad30{padding-right: 30px !important;}body[yahoo] .fontResize17{font-size:' \
               '17px !important;}}body{margin: 0px; padding: 0px;}*{-webkit-text-size-adjust: none;}.ExternalC' \
               'lass *{line-height: 100%;}.appleFix a{color: #000000 !important; text-decoration: none !import' \
               'ant;}td{mso-line-height-rule: exactly;}@media only screen and (max-width: 480px){body{width: 1' \
               '00%; min-width: 100%;}body[yahoo] .marginfix{position: relative; top: 0; left: 0; right: 0;}bo' \
               'dy[yahoo] .full-width-content{width: 300px !important; min-width: 300px !important; -webkit-bo' \
               'x-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;}body[yahoo] .hide{w' \
               'idth: 0px !important; height: 0px !important; display: none !important;}body[yahoo] .stack{dis' \
               'play: block !important; width: 100% !important; -webkit-box-sizing: border-box; -moz-box-sizin' \
               'g: border-box; box-sizing: border-box;}body[yahoo] .pad15{padding-left: 15px !important; paddi' \
               'ng-right: 15px !important;}body[yahoo] .pad20{padding-left: 20px !important; padding-right: 20' \
               'px !important;}body[yahoo] .nopadding{padding: 0px !important;}body[yahoo] .alignCenter{text-a' \
               'lign: center !important; margin: 0 auto !important;}body[yahoo] .alignLeft{text-align: left !' \
               'important;}body[yahoo] span.mobileTITLE1{font-size: 17px !important;}body[yahoo] span.mobileTI' \
               'TLE2{font-size: 15px !important;}body[yahoo] span.mobileTITLE3{font-size: 13px !important;}bod' \
               'y[yahoo] span.mobileCTA{font-size: 18px !important;}body[yahoo] .CAP{text-transform: capitaliz' \
               'e !important;}body[yahoo] .stack img, img.shrink{max-width: 100% !important; height: auto !imp' \
               'ortant;}body[yahoo] img.shrink{width: 100% !important; height: auto !important;}}</style> </he' \
               'ad> <body style="margin: 0px; -webkit-text-size-adjust:none; background-color: #dddddd;" yahoo' \
               '="fix"> <table cellpadding="0" cellspacing="0" border="0" width="100%"> <tr> <td align="center' \
               '" bgcolor="#dddddd" style="padding: 0px 20px;" class="nullPad"> <table border="0" bgcolor="#ff' \
               'ffff" cellspacing="0" cellpadding="0" width="600" class="container"> <tr> <td align="right" styl' \
               'e="padding:20px 30px 20px; background-color:#1e252b;" class="pad20"> <table cellpadding="0" cells' \
               'pacing="0" border="0" width="100%"> <tr> <td align="left" style="padding:40px 30px 40px; backgroun' \
               'd-color:#1e252b;"> <table cellpadding="0" cellspacing="0" border="0" width="100%"> <tr> <td align=' \
               '"center" style="font-family: Arial, Helvetica, sans-serif; color:#ffffff; font-size:20px;"> <span ' \
               'class="mobileTITLE1"> Новые сообщения от Huawei E3372h </span> </td></tr></table> </td></tr></tabl' \
               'e> </td></tr></table> </td></tr></table> <table cellpadding="0" cellspacing="0" border="0" width=' \
               '"100%"> <tr> <td align="center" bgcolor="#dddddd" style="padding: 0px 20px;" class="nullPad"><tab' \
               'le border="0" bgcolor="#1e252b" cellspacing="0" cellpadding="0" width="600" class="container"><tr' \
               '> <td align="center" style="padding:0px 30px 40px; background-color:#1e252b;" class="pad20">'

        for value in data:
            string = '<table cellpadding="0" cellspacing="0" border="0" width="100%"> <tr> <td align="left" style="' \
                     'padding:20px 25px 0px; background-color:#ffffff;"> <table cellpadding="0" cellspacing="0" bord' \
                     'er="0" width="100%"> <tr> <td align="right" class="pad20" style="padding: 0px 20px;"> <table c' \
                     'ellpadding="0" cellspacing="0" border="0" width="100%"> <td align="left" valign="top" style="fo' \
                     'nt-family: Arial, Helvetica, sans-serif; color:#000000; font-size:14px; line-height:20px; pad' \
                     'ding-bottom:30px; border-bottom:2px solid #cecece;" class="body-text"> <table cellpadding="0"' \
                     ' cellspacing="0" width="100%" style="min-width: 100%;" class="stylingblock-content-wrapper">' \
                     ' <tr> <td class="stylingblock-content-wrapper camarker-inner"> <tr align="left"> <td style="p' \
                     'adding:10pt .75pt 0pt 0pt"> <table width="100%" bgcolor="#EEEEEE"> <tr> <td style="padding:7.' \
                     '5pt 7.5pt 0pt 11.5pt"> <p style="font-size:9.5pt;font-family:Arial,sans-serif"> Отправитель: ' \
                     '<strong>{}</strong> </p><p style="font-size:9.5pt;font-family:Arial,sans-serif"> Дата: <str' \
                     'ong>{}</strong> </p></td></tr><tr> <td style="padding:5pt 7.5pt 3pt 14.5pt"> <p style="font-si' \
                     'ze:10.5pt;font-family:Arial,sans-serif">{}</td></tr></table></td></tr></td></tr></table></td><' \
                     '/table> </td></tr></table> </td></tr><tr> <td align="center"> <img src="http://newsletters-cd' \
                     'n.ea.com/origin/rtmtest2/images/feather_bottom.jpg" border="0" style="display:block;" class="' \
                     'shrink" alt=""> </td></tr></table>'.format(value['sender'], value['date'], value['msg'])
            text += string

        text += '</td></tr></table> </td></tr></table></body></html>'
        return text


if __name__ == '__main__':
    pass
