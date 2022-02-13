import speedtest
wifi  = speedtest.Speedtest()
print("Wifi Download Speed: ", wifi.download())
print("Wifi Upload Speed: ", wifi.upload())