# Learn_ESP32_By_Raheel
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
