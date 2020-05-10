import Adyen
ady = Adyen.Adyen()
client = ady.client
client.xapikey = "AQElhmfuXNWTK0Qc+iSUk2o7orCXQY1I3wEMlJngVegxueSC9koTlxDBXVsNvuR83LVYjEgiTGAH-wfG1CRJ3jahhXUCsu6Fe33WKr21rljDeU6Tfp0NS9Ls=-P*Mn8bjD,4j8Ih2b"
client.platform = "test"
adyen = Adyen.Adyen()
adyen.client.xapikey = 'AQElhmfuXNWTK0Qc+iSUk2o7orCXQY1I3wEMlJngVegxueSC9koTlxDBXVsNvuR83LVYjEgiTGAH-wfG1CRJ3jahhXUCsu6Fe33WKr21rljDeU6Tfp0NS9Ls=-P*Mn8bjD,4j8Ih2b'

result = adyen.checkout.payment_methods({
'merchantAccount': 'Dance4lifeECOM',
'countryCode': 'NL',
'amount': {
'value': 1000,
'currency': 'EUR'
  },
'channel': 'Web',
})

print (result)

adyen = Adyen.Adyen()
adyen.client.xapikey = 'AQElhmfuXNWTK0Qc+iSUk2o7orCXQY1I3wEMlJngVegxueSC9koTlxDBXVsNvuR83LVYjEgiTGAH-wfG1CRJ3jahhXUCsu6Fe33WKr21rljDeU6Tfp0NS9Ls=-P*Mn8bjD,4j8Ih2b'
 
result = adyen.checkout.payments({
   'amount': {
      'value': 1000,
      'currency': 'EUR'
   },
   'reference': '123',
   'paymentMethod': {
      'type': 'scheme',
      'encryptedCardNumber': '371449635398431',
      'encryptedExpiryMonth': 'test_03',
      'encryptedExpiryYear': 'test_2030',
      'encryptedSecurityCode': 'test_7373'
   },
   'returnUrl': 'https://dance4life.com/checkout?shopperOrder=12xy..',
   'merchantAccount': 'Dance4lifeECOM'
})
print (result)
