#Set your X-API-KEY with the API key from the Customer Area.
import Adyen
adyen = Adyen.Adyen()
adyen.client.xapikey = 'AQElhmfuXNWTK0Qc+iSUk2o7orCXQY1I3wEMlJngVegxueSC9koTlxDBXVsNvuR83LVYjEgiTGAH-wfG1CRJ3jahhXUCsu6Fe33WKr21rljDeU6Tfp0NS9Ls=-P*Mn8bjD,4j8Ih2b'
 
result = adyen.checkout.payments({
   'amount': {
      'value': 1000,
      'currency': 'EUR'
   },
   'reference': 'abc654',
   'paymentMethod': {
      'type': 'ideal',
      'issuer': '0721'
   },
   'returnUrl': 'https://www.dance4life.com',
   'merchantAccount': 'Dance4lifeECOM'
})

print (result)
