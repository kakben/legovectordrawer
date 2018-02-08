import pigpio

pi = pigpio.pi()

for g in range(0,32):
   print("gpio {} is {}".format(g, pi.read(g)))

pi.stop()
