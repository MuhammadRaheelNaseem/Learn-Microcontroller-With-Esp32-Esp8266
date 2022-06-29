<div class="jumbotron alert-success"><h1>7.) Relay Module </h1></div>

![image](https://user-images.githubusercontent.com/63813881/176359880-a4ac0620-bc6c-4e61-a040-6fe1995a90d3.png)
![image](https://user-images.githubusercontent.com/63813881/176359902-3d4b3603-12db-40e7-b036-df10b8eb4107.png)

<div>
<p>The relay module shown in the previous photo has two connectors, each with three sockets: common (<span class="rnthl rntcblack">COM</span>), Normally Closed (<span class="rnthl rntclblue">NC</span>), and Normally Open (<span class="rnthl rntcyellow">NO</span>).</p>
<ul><li><strong>COM:</strong>&nbsp;connect the current you want to control (mains voltage).</li><li><strong>NC&nbsp;(Normally Closed):</strong>&nbsp;the normally closed configuration is used when you want the relay to be closed by default. The NC are COM pins are connected, meaning the current is flowing unless you send a signal from the ESP to the relay module to open the circuit and stop the current flow.</li><li><strong>NO&nbsp;(Normally Open):</strong>&nbsp;the normally open configuration works the other way around: there is no connection between the NO and COM pins, so the circuit is broken unless you send a signal from the ESP to close the circuit.</li></ul>
</div>

# `Circuit Diagram:`

![image](https://user-images.githubusercontent.com/63813881/176359928-3dd16e11-84c3-46bf-bf69-d9d70594c218.png)

# `Code: 1`

<pre>
from machine import Pin
from time import sleep

# ESP32 GPIO 26
relay = Pin(26, Pin.OUT)

# ESP8266 GPIO 5
#relay = Pin(5, Pin.OUT)

while True:
  # RELAY ON
  relay.value(0)
  sleep(10)
  # RELAY OFF
  relay.value(1)
  sleep(10)
</pre>

# `Code: 2`
<pre>
from machine import Pin
from time import sleep

# ESP32 GPIO 26
relay = Pin(26, Pin.OUT)

# ESP8266 GPIO 5
#relay = Pin(5, Pin.OUT)

while True:
  relay.on()
  sleep(2)
  relay.off()
  sleep(2)
</pre>

# `Code: 3`
<pre>
from machine import Pin
from time import sleep

# ESP32 GPIO 26
relay = Pin(26, Pin.OUT)

# ESP8266 GPIO 5
#relay = Pin(5, Pin.OUT)

while True:
  relay.value(not relay.value())
  sleep(4)
</pre>
