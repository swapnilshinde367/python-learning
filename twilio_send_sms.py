# pylint: skip-file
# send sms using twilio service

from twilio.rest import Client

def handleSendSms():

    strAccountSid = '*******************************'
    strAuthToken = '********************************'
    objClient = Client( strAccountSid, strAuthToken )

    objMessage = objClient.api.account.messages.create(
                    to      = '+60++++++++++',
                    from_   = '+1++++++',
                    body    = 'Its rainning in KL!')
    print( objMessage )

handleSendSms()