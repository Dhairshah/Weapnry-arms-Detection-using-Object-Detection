from twilio.rest import Client

# accoutn sid and auth token
account_sid = ''
auth_token = ''

target_number = ['123456789', '987654321']

def send_sms():
    client = Client(account_sid, auth_token)

    for number in target_number:
        message = client.messages.create(
            body = "Alert! Knife or gun has been detected!",
            from_ = twilio_number,
            to = number)
        print('SMS send to ', number, '!')
        print(message.body)
        print(message.sid)