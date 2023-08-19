import requests
import RPi.GPIO as GPIO
import time

# Konfigurasi sensor PIR
PIR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Ubidots token dan URL
TOKEN = "BBFF-FYW5XH9qOibbuJSHBnX11W6JfBnL1a"  # Ganti dengan token Ubidots Anda
DEVICE_LABEL = "sic4-desi"  # Ganti dengan label perangkat Anda di Ubidots
VARIABLE_LABEL = "sensor-pir"  # Ganti dengan label variabel Anda di Ubidots

# Fungsi untuk membaca data sensor PIR
def read_pir_sensor():
    return GPIO.input(PIR_PIN)

# Fungsi untuk mengirim data ke Ubidots
def send_data_to_ubidots(data):
    url = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/{VARIABLE_LABEL}/values"
    headers = {"X-Auth-Token": TOKEN}
    payload = {"value": data}

    # Kirim permintaan POST ke Ubidots
    response = requests.post(url, headers=headers, json=payload)
    return response

# Main loop
try:
    while True:
        pir_value = read_pir_sensor()
        response = send_data_to_ubidots(pir_value)
        print("PIR value sent to Ubidots, Response:", response)
        time.sleep(5)  # Kirim data setiap 5 detik
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
