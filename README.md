Raspberry Pi Pico DHT11 Server

Items Required

- Raspberry Pi Pico W
- DHT11 Temperature/Humidity Sensor
- Breadboard, Jumperwire, Wi-Fi Connection
- Thonny IDE

Download Thonny IDE https://thonny.org/

Flash Micropython to your Raspberry Pi Pico W
- hold down the boot Button on the Pi Pico W, plug it into your computer, 
and let go of the boot button. You should see RP1/RP2 pop in your folders.
- open thonny and navigate to run at the top right
- click Configure Interpreter 
    - Under Which Kind of Interpreter Choose MicroPython (Raspberry Pi Pico)
    - click install or update
    - The Target Volume will be the RP1/RP2
    - MicroPython family RP2
    - varaint Pi Pico W / WH
    - version use the most recent
    - click install
    - exit back to the main page

Thonny Board Reconization (After Flashing)
- Click Configure Interpreter 
    - Click Port or WebREPL
    - Choose the COMS port shown
    - exit out to the main thonny page
    - press red stop sign 
    - Look at the Serial Shell to see your board information

DHT PINOUTS
    - VCC -> 3.3v (PIN 36)
    - GND -> GND (PIN 38)
    - S/AO-> GPIO 15 (PIN 20)

Navigate to Tools
    - Manage Packages
    - Type "dht" and click
    - Install
    - there should be a file stored onto the pico device called "dht.py"


The first file, "Pi_Pico_DHT11.py", is an example to test the sensor and connections, and does not need to be on the pi itself.
     - We wait two seconds (sleep(2)) to take our first reading with a debugging error.
       If you get this error, make sure you have wired correctly and saved the "dht.py" onto the device.


The second file, "dht11_picow_http.py", is a sample server to observe the dht11 hosted by the Pi Pico W using its Wi-Fi chip. 
We create an http landing page with the data from the dht11 updating every minute.
    - Replace the ssid and password with your ssid and password
    - Observe the Serial Shell for an address to enter into a browser on the same wifi
        ex. 198.xxx.x.322

 To have the Raspberry Pi Pico run "dht11_picow_http.py" on boot without needing to navigate to Thonny,
rename the file to "boot.py" and save it to the device.
    - File
        - Save As
        - Save to Device

To stop the boot.py, re-flash the board.
