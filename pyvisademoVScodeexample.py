import pyvisa as visa
import time

def check_op_complete():
    temp_values = MXR608Ademo.query_ascii_values('*OPC?')
    opc = int(temp_values[0])
    print (opc)
    #time.sleep(.5)

rm = visa.ResourceManager("/opt/keysight/iolibs/libktvisa32.so")
#rm = visa.ResourceManager()
#MXR608Ademo = rm.open_resource('TCPIP0::10.81.216.126::inst0::INSTR')
MXR608Ademo = rm.open_resource('TCPIP0::10.81.216.126::hislip0,4880::INSTR')


idn = MXR608Ademo.query('*IDN?')
print(idn)

MXR608Ademo.timeout = 10000
MXR608Ademo.write('*RST')
check_op_complete()
MXR608Ademo.write(':TIMebase:SCALe %G' % (1e-08))
check_op_complete()


MXR608Ademo.write(':DIGItize')
check_op_complete()

MXR608Ademo.write(':AUToscale:VERTical %s' % ('CHANNEL1'))
check_op_complete()


MXR608Ademo.write(':CHANnel1:INPut %s' % ('DC50'))
check_op_complete()


MXR608Ademo.write(':AUToscale:VERTical %s' % ('CHANNEL1'))
check_op_complete()
MXR608Ademo.write(':DIGItize')
check_op_complete()


MXR608Ademo.close()

rm.close()

# end of Untitled