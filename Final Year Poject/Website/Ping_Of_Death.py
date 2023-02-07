import os
import subprocess
import time
  
def ping(host, duration, packet_size):
      end_time = time.time() + duration
      while time.time() < end_time:
          result = subprocess.run(['ping', '-s', str(packet_size), host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          if result.returncode == 0:
              print("Ping successful")
          else:
              print("Ping failed")
  
host = input("Enter the target host: ")
duration = int(input("Enter the duration (in seconds) for which to ping the target: "))
ping(host, duration, 65507)