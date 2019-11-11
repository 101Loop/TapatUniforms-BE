from sendsms.backends.base import BaseSmsBackend


def send_sms(message: str, mobile: list):
    import requests

    if len(mobile) < 1:
        raise ValueError("Need atleast one mobile number")

    params = {
        "AUTH_KEY": "5031ad8169211b14d3937ed0d32df1",
        "message": message,
        "senderId": "USMSCO",
        "routeId": "1",
        "mobileNos": ",".join(mobile),
        "smsContentType": "english",
    }

    url = "http://msg.msgclub.net/rest/services/sendSMS/sendGroupSms"
    resp = requests.get(url, params=params)

    try:
        resp = resp.json()
    except:
        raise ValueError("Unable to send SMS")
    else:
        if str(resp["responseCode"]) != "3001":
            raise ValueError("Sending sms failed")

    return


class MsgClubBackend(BaseSmsBackend):
    def send_messages(self, messages):
        for message in messages:
            for to in message.to:
                try:
                    send_sms(message=message.body, mobile=[to])
                except:
                    if not self.fail_silently:
                        raise
