# garageDoor

This is my hobby project. The main idea of the project is opening the garage door by using my mobile phone. 

Required Hardware
- Raspberry pi 2 ~$40
- Single channel relay (I used two channel relay) ~$2.5
- Jumper wires ~$1
- Garage door controller


0. Layout
![Image of Layout](https://github.com/ykulah/garageDoor/blob/master/docu/layout.jpg)
1. Hardware Installation

My remote controller is shown in the figure. I soldered a jumper cable both end of the button. These two cables will be connected to relay. The connection of relay and raspberrypi is also easy. Raspberrypi provides 5V and GND outputs for relay. Signal input of relay is the GPIO18 pin for my case.

<img src="docu/remote.jpg" width="300">
<img src="docu/relay.jpg" width="250">
<img src="docu/raspberrypi.jpg" width="300">

2. Server 

I used Python API of raspberry's GPIO pins and the server is also implemented in Python by using [Flask](http://flask.pocoo.org/). In order to run server, first update the passphrase of your server in the code. Then run;

<code>python doorServer.py</code>

Before server start, you can see the <code>key</code> of your garage door in terminal.

By default server is running on <code>:8080</code> port of your raspberrypi.

You can open your garage door by using following address in browser;

<code>http://< IPofYourRaspberry >:8080/openDoor/< key ></code>

3. Network
