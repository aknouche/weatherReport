import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client

password = input("Please enter your email password: ")
def sendEmailRain():
    msg = MIMEMultipart()
    msg['From'] = 'lamine.aknouche@malmo.se'
    msg['To'] = 'ml.aknouche@gmail.com'
    msg['Subject'] = 'Risk för regn!'
    message = 'Risk för regn. Kom ihåg paraply och regnkläder'
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp-mail.outlook.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    #password = input("Please enter your email password: ")
    mailserver.login('lamine.aknouche@malmo.se', password)

    mailserver.sendmail('lamine.aknouche@malmo.se','ml.aknouche@gmail.com',msg.as_string())

    mailserver.quit()

def sendSmsRain():    

    try:
        accountSID = 'AC620e24ce9259f3712bd893cf0391c8bf'
        authToken = '3fc430940fbc26b0bd9ec4e1428cc397'
        twilioCli = Client(accountSID, authToken)
        myTwilioNumber = '+46790645826'
        myCellPhone = '+46722515715'
        message = twilioCli.messages.create(body='Risk för regn. Kom ihåg paraply och regnkläder!', from_=myTwilioNumber, to=myCellPhone)
    except:
        print("SMS was not sent")


def sendEmailCold():
    msg = MIMEMultipart()
    msg['From'] = 'lamine.aknouche@malmo.se'
    msg['To'] = 'ml.aknouche@gmail.com'
    msg['Subject'] = 'Burr va kallt!'
    message = 'Det kan bli kallt, ta på varma kläder! Skippa cykeln!'
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp-mail.outlook.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    # password = input("Please enter your email password: ")
    mailserver.login('lamine.aknouche@malmo.se', password)

    mailserver.sendmail('lamine.aknouche@malmo.se','ml.aknouche@gmail.com',msg.as_string())

    mailserver.quit()

def sendSmsCold():    

    try:
        accountSID = 'AC620e24ce9259f3712bd893cf0391c8bf'
        authToken = '3fc430940fbc26b0bd9ec4e1428cc397'
        twilioCli = Client(accountSID, authToken)
        myTwilioNumber = '+46790645826'
        myCellPhone = '+46722515715'
        message = twilioCli.messages.create(body='Det kan bli kallt, ta på varma kläder! Skippa cykeln', from_=myTwilioNumber, to=myCellPhone)
    except:
        print("SMS was not sent")

        
def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
    return res.json();
def print_weather(result,city):
    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    
    skies = result['weather'][0]['main']
    if skies != 'Clear':
        sendEmailRain()
        #sendSmsRain()
    
    temprature = result['main']['temp']
    if temprature < 0:
        sendEmailCold()
        #sendSmsRain()
        
        
    
def main():
    city="Malmö"
    try:
        query='q='+city;
        w_data=weather_data(query);
        print_weather(w_data, city)
        print()
    except:
        print('City name not found...')

if __name__=='__main__':
    main()