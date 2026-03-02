import supervisor
import storage
import usb_cdc
import usb_hid
import usb_midi

supervisor.set_usb_identification(
	vid=0x03F0,
	pid=0x304A,
	manufacturer="HP Inc",
	product="Slim Keyboard"
)

# Disable the storage drive interface
storage.disable_usb_drive()

# Disable serial console interface
usb_cdc.disable()

# Disable audio and midi interfaces
usb_midi.disable()

# Make RP2040-Zero look like a real keyboard (for our evil input), let the real mouse present itself as itself 
usb_hid.enable((usb_hid.Device.KEYBOARD))
