
import time
import random

import predix.app
import predix.data.timeseries

# You can customize these if you feel fancy
min_voltage = 200
max_voltage = 240
hertz = 1.0/1.0

# Load application context
app = predix.app.Manifest('manifest.yml')

# We will use Time Series to ingest data
ts = predix.data.timeseries.TimeSeries()

# Operate as a daemon and continuously generate and send data
while True:
    try:

        # Generate a random voltage value simulated from multiple sensors
        # and queue them up.
        for tag in ['Voltage:Sensor1', 'Voltage:Sensor2', 'Voltage:Sensor3']:
            value = random.randint(min_voltage, max_voltage)
            ts.queue(tag, value)
            print(tag, value)

        # Send readings from all 3 sensors to Time Series and then wait to
        # take another reading.
        ts.send()
        time.sleep(hertz)

    except KeyboardInterrupt:

        # Provide evidence data was being stored before exiting
        print(ts.get_tags())
        break
