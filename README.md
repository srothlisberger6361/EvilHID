# EvilHID
This material is provided for educational and defensive security purposes only. Any tools, techniques, or procedures demonstrated must be used exclusively in environments where you have explicit written authorization. Unauthorized access to computer systems is illegal and may result in criminal and civil penalties. The author assumes no liability for misuse.

![Alt Text](banner.jpg)

HID Keystroke injection for the RP2040-Zero designed to (upon plug in) create a minimized PowerShell window with high integrity Admin privileges, download and install an MSI. Then, the PowerShell process is exited. This 1) avoids using a hidden PowerShell window (-Hidden) from Win+R which might flag EDR/AV 2) legitimately minimizes user visibility 2) can register a windows service and 3) can give system-level access via that trusted service. 

## Make your own EvilHID

BLOG: 

- Hold down the BOOT button on your RP2040-zero and plug it in.
- Once you see the RPI-RP2 drive, drag the `adafruit-circuitpython-waveshare_rp2040_zero-en_US-10.0.3.uf2` file into it.
- The drive should then be flashed as CIRCUITPY
- In code.py- change ip address, port, and .msi file name
- Drag code.py and boot.py in src to the base drive
- Drag adafruit_hid folder in src to the lib folder
- Ready to go

Note: If you need to nuke and reflash, double click reset and you should see the drive named RPI-RP2 appear. Drag and drop flash_nuke.uf2 inside. You will have to reflash with adafruit-circuitpython-waveshare_rp2040_zero-en_US-10.0.3.uf2 and redrop code.py, boot.py, and adafruit_hid library in the CIRCUITPY drive.
