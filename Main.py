import time
from plyer import notification

def remind_to_drink():
    while True:
        notification.notify(
            title="💧 Time to Drink Water!",
            message="Stay hydrated! Drinking water is essential for your health. Take a sip now! 🥤",
            timeout=10
        )
        time.sleep(60 * 60)  # Wait for 1 hour (3600 seconds)

if __name__ == "__main__":
    remind_to_drink()
