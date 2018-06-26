from twilio.rest import TwilioRestClient

#Envia SMS, necessario criar conta gratis n twilio


account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+5511999991111",    # Mudar para seu numero de celular
    from_="+") # Mudar para numero fornecido pelo twilio

print(message.sid)
