# `Learn IoT With Esp32 | Esp8266 By Raheel`

1. **Introduction to Embedded Systems**
2. **Introduction to Microcontroller Esp32 | Esp8266 | Raspberry pi Pico | RP 2040.**
3. **Serial Data communication**
4. **IoT Communication Devices (IR)**
5. **Radio Frequency Communication**
6. **RF Communication Application**
7. **RFID Applications**
8. **LORA Module and its Application**
9. **Preparation steps of Microcontroller Esp32 | Esp8266**
10. **Introduction to micropython.**
11. **Difference between Python & Micropython.**
12. **Making a simple program of LED.**
13. **Controlling LED with microcontroller.**
14. **How to connect Push Button to the microcontroller.**
15. **Making Push Button game.**
16. **Controlling Buzzer into the microcontroller.**
17. **Making Morse Code sound with buzzer**
18. **Connectivity of Distance Sensor | Motion Sensor.**
19. **Making a program for unknown object detection with a motion sensor.**
20. **Motion sensor connects with buzzer and LED.**
21. **Connectivity of Temperature Sensor**
22. **Make a program of the LED when the temperature raise.**
23. **Connectivity of Relay Module**
24. **Controlling electrical equipment with the relay module.**
25. **Connectivity of LCD 16x2.**
26. **Printing message and DHT reading into LCD 16x2.**
27. **Connectivity IR sensor.**
28. **Making line the following robot with IR Sensor.**
29. **Connecting of Smoke Sensor.Connectivity of Smoke Sensor.**
30. **Connectivity of LDR Sensor | L298D motor driver.**
31. **Controlling DC Motors with L298D |  Servo motor.**
32. **Connectivity of Voltage Sensor | Potentiometer.**
33. **Controlling LED brightness with Potentiometer.**
34. **Connectivity of DHT sensor**
35. **Introduction to Cloud Platform with respect to IoT**
36. **How many types of clouds can be used in IoT**
37. **What is Firebase and how to send data and fetch from firebase**
38. **Introduction to Blynk and How to use it and how to control IoT device with respect to blynk**
39. **Introduction to ThingSpeak and How to send reading from IoT sensor to ThingSpeak**
40. **Use of Vonage API for OTP in IoT Device**


# `Introduction to Embedded Systems:`
Embedded systems are computer systems designed to perform specific tasks within larger devices or systems. They consist of a microcontroller or microprocessor, memory, input/output interfaces, and sensors. Programming embedded systems requires knowledge of low-level languages like C or C++. The article emphasizes the importance of embedded systems in enabling the Internet of Things (IoT) by connecting devices and collecting data. It also discusses the challenges of developing embedded systems, such as hardware-software integration and meeting specific requirements.

Overall, embedded systems are specialized computer systems with dedicated functions, real-time constraints, and limited resources. They play a crucial role in various industries and require expertise in low-level programming languages for their development. 
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/28464248-bf1e-466c-8287-742862721006)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/b95a4e51-7f38-444a-b41a-19e884a2cf25)


# `Getting Start With Esp32` 
# `What is Esp32`

`ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth`

![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/f26a1603-e6f4-4c9d-865f-4e43398199c6)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/80fb0459-af7b-47a0-ad1a-89a7410ea5cc)



# `ESP32 GPIO Pins:`
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/dde16da8-8385-4a23-9755-63bb9813e2ab)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/14fd318e-05b9-4649-aa0b-e05037d5c10c)


# `Difference Between Esp32 | Esp8266`
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/d1ff53d8-a745-4788-994a-311eaa48176e)

The ESP32 is an upgrade over the ESP8266 and includes 34 GPIO pins along with a 160 MHz Xtensa dual-core processor. A 32-bit processor, an ultra-low power co-processor, and several input/output ports, including digital-to-analog converters, are all features of the ESP32.

`or`

The ESP32 and ESP8266 are both popular Wi-Fi and Bluetooth-enabled microcontrollers developed by Espressif Systems. Here are the key differences between the two:

1. **Performance**: The ESP32 is more powerful than the ESP8266 in terms of processing power, memory, and clock speed. It has a dual-core processor and offers more RAM and flash memory, allowing it to handle more complex tasks.

2. **Wi-Fi**: Both the ESP32 and ESP8266 support Wi-Fi connectivity, but the ESP32 offers dual-band Wi-Fi (2.4 GHz and 5 GHz) while the ESP8266 supports only 2.4 GHz Wi-Fi.

3. **Bluetooth**: The ESP32 includes Bluetooth Classic and Bluetooth Low Energy (BLE) support, making it suitable for a wider range of IoT applications. The ESP8266 does not have built-in Bluetooth capabilities.

4. **GPIO Pins**: The ESP32 has more GPIO pins compared to the ESP8266, providing greater flexibility for connecting external devices and sensors.

5. **Power Consumption**: The ESP8266 generally consumes less power than the ESP32, making it suitable for applications where power efficiency is a priority.

6. **Price**: The ESP8266 is generally cheaper than the ESP32, which can make it a more cost-effective choice for simpler projects.

Overall, the ESP32 is a more advanced and feature-rich microcontroller compared to the ESP8266. It offers improved performance, dual-band Wi-Fi, Bluetooth support, and more GPIO pins, but at a slightly higher cost. The choice between the two depends on the specific requirements of your project and the features you need.


# `What is MicroPython?`
`MicroPython is a re-implementation of Python 3 targeted for microcontrollers and embedded systems. MicroPython is very similar with regular Python. So, if you already know how to program in Python, you also know how to program in MicroPython.`

![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/12f2d391-7dcc-49e2-97e1-3eadb6356951)



`Apart from a few exceptions, the language features of Python are also available in MicroPython. The biggest difference between Python and MicroPython is that MicroPython was designed to work under constrained conditions.`

`Because of that, MicroPython does not come with the full standard library. It only includes a small subset of the Python standard library. However, it does include modules to access low-level hardware – this means that there are libraries to easily access and interact with the GPIOs.`

`Additionally, devices with Wi-Fi capabilities like the ESP8266 and ESP32 include modules to support network connections.`

# `Why MicroPython?`
`Python is one of the most widely used, simple and easy-to-learn programming languages around. So, the emergence of MicroPython makes it extremely easy and simple to program digital electronics. If you’ve never programmed digital electronics before, MicroPython is a good starting point.`

`MicroPython’s goal is to make programming digital electronics as simple as possible, so it can be used by anyone. Currently, MicroPython is used by hobbyists, researchers, teachers, educators, and even in commercial products. The code for blinking an LED on a ESP32 or ESP8266 is as simple as follows:`

# `How Many Microcontrollers Support Micropython`
MicroPython, a lean and efficient implementation of the Python programming language for microcontrollers and embedded systems, supports a wide range of microcontrollers. It is designed to be compatible with various microcontroller architectures, including but not limited to:

1. **ARM Cortex-M (e.g., STM32, NXP LPC, Nordic nRF)**
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/5bb81515-d3d3-4b60-b4cc-f5d9ce2c9d7f)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/dce0f302-8159-4283-ab6b-bc35e35b4296)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/fd7ae667-e7b3-479d-92fc-2c10cbb595a8)

2. **ESP32 and ESP8266**
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/1a9905b0-5bf5-4ced-92af-ef58e17567db)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/58417d90-5393-4b3b-b873-90440675ab4b)

3. **Microchip PIC32**
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/25ba72c2-0689-451c-9160-f459da1289a9)

4. **Atmel AVR and SAMD (e.g., Arduino boards)**
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/93497950-5ba2-4d91-9378-4ddbf2107d8e)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/ab51af63-fe8b-4a16-96ef-d1aa817a1108)
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/c97fb7dd-ba2d-42ed-b71d-b0a3ad8dcf1c)

5. **Teensy boards**
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/80b032e0-2cc8-4bfb-a5a8-f1a8a334ff3b)

6. **Raspberry Pi Pico (RP2040)**
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/3a44600f-0305-4d3b-9ca9-8c981e484015)

7. **Pyboard (official MicroPython board)**
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/07fc58cd-f883-4203-95fb-958c22a0139b)


# `What is Serial Data Communication and it used of in IoT`
Serial data communication is a method of transferring data between two devices or systems by sending the data one bit at a time over a single communication channel. It involves the sequential transmission of data, where each bit is sent one after another in a specific order. It is commonly used in various applications, such as computer networking, industrial automation, embedded systems, and telecommunications. There are different serial communication protocols, such as RS-232, RS-485, SPI, I2C, and UART, each with its own specifications and characteristics. Serial communication is used in IoT (Internet of Things) systems to connect and communicate with various IoT devices and components.
Serial communication is a key use case in the Internet of Things (IoT). It allows IoT devices to interface with sensors, actuators, and other peripherals, enabling the exchange of data. Data transmission is used to transmit data between IoT devices and gateways or central systems. Configuration and firmware updates are often used for device configuration and firmware updates. Protocols and interfaces rely on serial communication, and legacy device integration is essential for integrating legacy devices into IoT networks. Overall, serial communication in IoT enables seamless connectivity, data exchange, and control between IoT devices, sensors, and central systems, enhancing the interoperability and functionality of IoT solutions.
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/42b86fb8-5b4f-4d46-9359-d4fb3d6734d5)


# `What is Radio Frequency (RF) communication:`
1. Radio Frequency (RF) communication in IoT refers to the wireless transmission and reception of data using radio frequency signals.
2. It is a method of communication that allows IoT devices to exchange information over a wireless medium using radio waves.
3. RF communication is widely used in IoT systems due to its ability to provide long-range connectivity, support for multiple devices, and reliable data transmission.
4. In RF communication, IoT devices use radio frequency bands to transmit and receive data.
5. These devices typically have RF transceivers that enable them to transmit and receive signals in the specified frequency range.
5. RF communication in IoT can be implemented using various wireless protocols such as Wi-Fi, Bluetooth, Zigbee, LoRaWAN, and cellular technologies like 2G, 3G, 4G, and 5G.RF communication in IoT offers several advantages.
5. It enables seamless wireless connectivity between IoT devices, allowing them to communicate and exchange data over extended distances.
5. It also provides flexibility in device placement and eliminates the need for physical wired connections.
5. RF communication is suitable for a wide range of IoT applications, including smart homes, industrial automation, agriculture, healthcare, and smart cities.
5. However, RF communication in IoT also has challenges, such as signal interference, limited bandwidth, and power consumption.
5. These factors need to be considered and optimized to ensure reliable and efficient communication in IoT deployments.
5. Overall, RF communication plays a crucial role in enabling wireless connectivity and data exchange in IoT systems, facilitating the growth and expansion of the IoT ecosystem.
![image](https://github.com/MuhammadRaheelNaseem/Learn_ESP32_By_Raheel/assets/63813881/a6319ac2-3d9e-400a-b7b8-e19975b31bf4)


# `RFID and it's Applications`
Radio Frequency Identification (RFID) is a form of wireless communication that uses electromagnetic or electrostatic coupling in the radio frequency portion of the electromagnetic spectrum to uniquely identify an object, animal, or person. It is a method that is used to track or identify an object by radio transmission over the web. There are many kinds of RFID, each with different properties, but the most fascinating aspect of RFID technology is that most RFID tags have neither an electric plug nor a battery. UHF RHID (Ultra-High Frequency RFID) is used on shipping pallets and some driver’s licenses. HF RFID (high-frequency RFID) operates at 13.56 MHz and is likely to be in passports, credit cards, books, and noncontact payment systems. LF RFID (low-frequency RFID) was developed before HF RFID and used for animal tracking.There are two types of RFID:
**1. Passive RFID:**
Passive RFID tags do not have their own power source but instead use power from the reader. The RF tags are emitted from active antennas and use specific frequencies such as 125–134 MHZ, 13.56 MHZ, and 856 MHZ to 960 MHZ.
**2. Active RFID:**
RF tags are attached to a power supply that emits a signal and an antenna that receives the data. Active tags have their own power source and do not require power from the source or reader.

**Working Principles of RFID:**
RFID uses radio waves to perform AIDC technology, which stands for Automatic Identification and Data Capture. An antenna converts power into radio waves, which are used to communicate between readers and tags. RFID readers retrieve the information from the tag, which detects the tag and reads or writes the data into the tag. It may include one processor, package, storage, transmitter, and receiver unit.

**Working with RFID:**
RFID systems consist of three components: a scanning antenna, a transceiver, and a transponder. The RFID reader is a network-connected device that uses radio waves to transmit signals that activate the tag. Once activated, the tag sends a wave back to the antenna, where it is translated into data. The read range for RFID tags varies based on factors such as the type of tag, type of reader, RFID frequency, and interference in the surrounding environment. Tags with a stronger power source also have a longer reading range.

**Features of RFID:**
1. An RFID tag consists of two parts: a microcircuit and an antenna.
2. This tag is covered by protective material, which acts as a shield against the effects of the outer environment.
3. This tag may be active or passive, in which case we mainly and widely use passive RFID.

**Application of RFID:**
1. It is utilized for tracking shipping containers, trucks, and railroad cars.
2. It is used in asset tracking.
3. It is used in the form of a credit card for accessing applications.
4. It is used in personnel tracking.
5. Controlling access to restricted areas.
6. It uses ID badges.
7. Supply chain management
8. Counterfeit prevention (e.g., in the pharmaceutical industry).

**Advantages of RFID:**
1. It provides data access and real-time information without taking too much time.
2. RFID tags follow instructions and store a large amount of information.
3. The RFID system is a non-line-of-sight technology.
4. It improves the efficiency and traceability of production.
5. In RFID, hundreds of tags are read in a short time.

**Disadvantages of RFID:**
1. It takes longer to program RFID devices.
2. RFID can be intercepted easily, even if it is encrypted.
3. In an RFID system, there are two or three layers of ordinary household foil to block the radio wave.
4. There is a privacy concern about RFID devices. Anyone can access information about anything.
5. Because of the battery, active RFID can be more expensive.

# `LORA Module and its Application:`

The LoRa module is a wireless communication module that utilizes the Long Range (LoRa) modulation technique for long-range and low-power communication. It operates in the unlicensed ISM bands, allowing for widespread deployment and flexibility.
it also offers a versatile and cost-effective solution for various applications requiring long-range, low-power, and reliable wireless communication.

**Applications of LoRa modules include:**
1. **Internet of Things (IoT):** LoRa modules are widely used in IoT applications for long-range connectivity and low-power operation. They enable various IoT devices to transmit sensor data over long distances, making them suitable for smart cities, agriculture, environmental monitoring, and asset tracking.
2. **Smart Metering:** LoRa modules are used in smart metering systems for remote monitoring and management of utility meters, such as electricity, water, and gas meters. They provide a cost-effective and efficient solution for collecting consumption data.
3. **Industrial Automation:** LoRa modules are employed in industrial automation to enable wireless communication between devices and control systems. They can be used for remote monitoring, control, and data acquisition in industries such as manufacturing, logistics, and transportation.
4. **Smart Buildings:** LoRa modules find applications in smart buildings for monitoring and controlling various systems, including lighting, HVAC (heating, ventilation, and air conditioning), occupancy sensing, and energy management. They facilitate energy efficiency and improve occupant comfort.
5. **Environmental Monitoring:** LoRa modules are utilized for environmental monitoring applications, including air quality monitoring, weather stations, and water quality monitoring. They enable real-time data collection from remote locations, contributing to environmental sustainability and resource management.
6. **Asset Tracking:** LoRa modules are used for asset tracking applications, such as tracking vehicles, containers, and valuable assets. They provide long-range connectivity and low-power operation, allowing for efficient tracking and management of assets.


The high-level option is MicroPython for ESP32. Where the user doesn't even really need to install anything on their computer: anything that can open a serial terminal will do. The Python language itself is much more beginner friendly than the C language used by Arduino and ESP-IDF.

# `Getting Start With Esp32` 
# `What is Esp32`
### `ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth`

![image](https://user-images.githubusercontent.com/63813881/175464150-0040b307-1d68-4bbd-a499-a0c77e261c3f.png)
![image](https://user-images.githubusercontent.com/63813881/175464167-d0e9f3e6-3a55-4bb4-91cc-fe9612e374b7.png)


# `ESP32 GPIO Pins:`

![image](https://user-images.githubusercontent.com/63813881/175464156-8d226744-e098-484d-895d-c4d4513d426c.png)
![image](https://user-images.githubusercontent.com/63813881/175464176-d7614c84-3a3d-461c-bc2c-6d386fa76f96.png)

# `What is MicroPython?`
`MicroPython is a re-implementation of Python 3 targeted for microcontrollers and embedded systems. MicroPython is very similar with regular Python. So, if you already know how to program in Python, you also know how to program in MicroPython.`

![image](https://user-images.githubusercontent.com/63813881/175464188-f23d4059-f92f-473f-8e5d-7bd96162c205.png)


`Apart from a few exceptions, the language features of Python are also available in MicroPython. The biggest difference between Python and MicroPython is that MicroPython was designed to work under constrained conditions.`

`Because of that, MicroPython does not come with the full standard library. It only includes a small subset of the Python standard library. However, it does include modules to access low-level hardware – this means that there are libraries to easily access and interact with the GPIOs.`

`Additionally, devices with Wi-Fi capabilities like the ESP8266 and ESP32 include modules to support network connections.`

# `Why MicroPython?`
`Python is one of the most widely used, simple and easy-to-learn programming languages around. So, the emergence of MicroPython makes it extremely easy and simple to program digital electronics. If you’ve never programmed digital electronics before, MicroPython is a good starting point.`

`MicroPython’s goal is to make programming digital electronics as simple as possible, so it can be used by anyone. Currently, MicroPython is used by hobbyists, researchers, teachers, educators, and even in commercial products. The code for blinking an LED on a ESP32 or ESP8266 is as simple as follows:`

# `Installing Thonny IDE:`
`In this guide, we provide instructions to install Thonny IDE in different operating systems, read the section that fits your needs:`

## `Installing Thonny IDE – Windows PC`
`To install Thonny on your Windows PC, follow the next instructions:`

`1. Go to ` https://thonny.org

`2. Download the version for Windows and wait a few seconds while it downloads.`

![image](https://user-images.githubusercontent.com/63813881/175464240-6a08c721-2e60-4499-94b8-8c6a9c823cb2.png)

`3. Run the .exe file.`

![image](https://user-images.githubusercontent.com/63813881/175464257-3d4660a9-6fec-4108-9ce5-72bc3f4e6485.png)

`4. Follow the installation wizard to complete the installation process. You just need to click “Next”.`

![image](https://user-images.githubusercontent.com/63813881/175464273-a1bff9b3-bc7f-46f4-9d41-fa5b3383235b.png)

`5. After completing the installation, open Thonny IDE. A window as shown in the following figure should open.`

![image](https://user-images.githubusercontent.com/63813881/175464287-cc8dc3c3-fbbc-42c4-84fa-86005be927b9.png)

# `Download USB Universal Driver:`

## `Goto this link and download`

![image](https://user-images.githubusercontent.com/63813881/175464306-d5b780e5-5ccb-4a4c-ab0e-27f6933304f8.png)
![image](https://user-images.githubusercontent.com/63813881/175464328-dacca926-9f57-4b84-b72a-33c8ace44d1e.png)
![image](https://user-images.githubusercontent.com/63813881/175464362-c9dc9862-64c5-4116-9368-aaef2d6c6c17.png)
![image](https://user-images.githubusercontent.com/63813881/175464377-dda562e5-55a6-4dd8-8b1d-0e5a8462bce1.png)
![image](https://user-images.githubusercontent.com/63813881/175464399-3afc9b87-d1f2-484c-af9c-74f32157d93a.png)


# `Downloading MicroPython Firmware`

## `Go to the MicroPython Downloads page:` https://micropython.org/download/.

`Select the type of board you’re using. Here are the quick links for “regular” ESP32 and ESP8266 boards:`

`ESP32 MicroPython firmware goto this link `https://micropython.org/download/esp32/ 

`You should see a similar web page (see figure below) with links to download .bin files. Download the latest release.`

![image](https://user-images.githubusercontent.com/63813881/175464539-2ee0e80d-faad-44a9-b949-7f21589e4a77.png)

# `Flashing MicroPython Firmware using Thonny IDE`

`In this section, you’ll learn how to flash MicroPython firmware on your boards using Thonny IDE. Follow the next steps:`

`1) Connect your ESP32 or ESP8266 board to your computer.`

![image](https://user-images.githubusercontent.com/63813881/175464563-07fabd2a-1e58-4b32-b71e-504f14e3ec65.png)

`2) Open Thonny IDE. Go to Run Options > Click Select Interpreter.`

![image](https://user-images.githubusercontent.com/63813881/175464586-002cecf2-ab4e-4d9f-b369-f70ddbe03e52.png)

`3) Select the interpreter you want to use accordingly to the board you’re using and select the COM port your board is connected to. Finally, click on the link Install or update firmware.`

`4) Select the port once again, and then click on the Browse button to open the .bin file with the firmware you’ve downloaded on the previous step. Select the options as shown in the picture below and finally click on Install.`

![image](https://user-images.githubusercontent.com/63813881/175464605-f147507a-98ad-49a4-805b-41281cadcad7.png)

![image](https://user-images.githubusercontent.com/63813881/175464651-ab7bd20b-2f1b-4b89-8fd9-73788b33d256.png)

![image](https://user-images.githubusercontent.com/63813881/175464670-236a8c0d-4637-4f34-8327-b757adc67441.png)

# `Now you can see Thonny IDE works fine`

![image](https://user-images.githubusercontent.com/63813881/175464686-5803aa63-b084-45d8-a3cf-6cb6979dc702.png)

# `Thonny IDE Overview`
# `At this point, you should have:`

`Thonny IDE installed on your computer`

`1.) ESP32/ESP8266 flashed with MicroPython firmware`

`2.) Open Thonny IDE. There are two different sections: the Editor and the MicroPython Shell/Terminal:`

![image](https://user-images.githubusercontent.com/63813881/175464704-1e494d0c-8fba-44df-af8f-dd08a384e30a.png)

`The Editor section is where you write your code and edit your .py files. You can open more than one file, and the Editor will open a new tab for each file.`

`On the MicroPython Shell you can type commands to be executed immediately by your ESP board without the need to upload new files. The terminal also provides information about the state of an executing program, shows errors related with upload, syntax errors, prints messages, etc…`

`You can also customize Thonny IDE to show other useful tabs. Go to View and you can select several tabs that provide more information.`

![image](https://user-images.githubusercontent.com/63813881/175464726-15a7fa33-7067-4a6b-b4b0-20af3817756e.png)

`Something that could be very useful is the Variables tab. It lists all available variables in your program and their corresponding values.`

# `Let's play with ESP32`

# `Breadboard`
`What is Breadboard?`

`A breadboard is used to build and test circuits quickly before finalizing any circuit design. The breadboard has many holes into which circuit components like ICs and resistors can be inserted. A typical breadboard is shown below:`

![image](https://user-images.githubusercontent.com/63813881/175464747-8596bd45-da30-4c19-b24d-258b3c381d5a.png)

# `Let's Start Coding`

<h3 align="left">Support:</h3>
<p><a href="https://www.buymeacoffee.com/muhammadraheel"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="Raheel" /></a></p><br><br>
