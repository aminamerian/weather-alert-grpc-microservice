import grpc
import notification_pb2_grpc
from notification_pb2 import WeatherAlert


def run():
    channel = grpc.insecure_channel("localhost:50052")
    user_notification_client = notification_pb2_grpc.UserNotificationServiceStub(
        channel
    )
    location = input("Enter location: ")
    temperature = float(input("Enter temperature: "))
    humidity = float(input("Enter humidity: "))
    wind_speed = float(input("Enter wind speed: "))

    alert = WeatherAlert(
        location=location,
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
    )
    response = user_notification_client.SendWeatherAlert(alert)
    print(f"Response: {response.message}")


if __name__ == "__main__":
    run()
