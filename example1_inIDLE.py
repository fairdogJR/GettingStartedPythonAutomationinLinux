import pyvisa as visa
import time
# start of Untitled


rm = visa.ResourceManager()
MXR608Ademo = rm.open_resource('TCPIP0::10.81.216.126::inst0::INSTR')
idn = MXR608Ademo.query('*IDN?')
print (idn)
MXR608Ademo.timeout = 10000
time.sleep(2)
print ("reset")
MXR608Ademo.write('*RST')
time.sleep(2)
print("autoscale")
MXR608Ademo.write(':AUToscale')
temp_values = MXR608Ademo.query_ascii_values('*OPC?')
opc = int(temp_values[0])
time.sleep(2)
print ("set input to dc 50 ohms")
MXR608Ademo.write(':CHANnel1:INPut %s' % ('DC50'))
print("autoscale")
MXR608Ademo.write(':AUToscale')

MXR608Ademo.close()
rm.close()

# end of Untitled