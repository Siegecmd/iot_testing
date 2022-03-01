import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)

def on_connect(client, userdata, flags, rc): #callbacks
    print("Connected with result code", rc)

broker_address="192.168.0.9"

client = mqtt.Client(client_id="siegecmd", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

client.username_pw_set(username="raptor_mqtt", password="PfuaSy3gfBze81PpcG/SfQ==")

client.on_message= on_message 
client.on_connect = on_connect

client.connect(broker_address,1883,0) 

client.subscribe("/siegecmd/subscribe")

client.loop()

timer = time.time()
while True:
    client.loop()
    try:
        if time.time() - timer >= 5:
            print("Publishing")
            client.publish("/siegecmd/publishtemp",30.0)
            timer = time.time()
    except Exception as e:
        print(e)