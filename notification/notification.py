import grpc
from concurrent import futures

import notification_pb2_grpc
from notification_pb2 import WeatherAlertConfirmation


class UserNotificationService(notification_pb2_grpc.UserNotificationServiceServicer):
    def SendWeatherAlert(self, request, context):
        # Implement logic to send weather alerts to users
        # For demonstration purposes, let's just print the alert
        location = request.location
        temperature = request.temperature
        humidity = request.humidity
        wind_speed = request.wind_speed
        print(
            f"Weather Alert for {location}: Temperature={temperature}, Humidity={humidity}, Wind Speed={wind_speed}"
        )
        return WeatherAlertConfirmation(
            success=True, message="Weather alert sent successfully"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notification_pb2_grpc.add_UserNotificationServiceServicer_to_server(
        UserNotificationService(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    print("User Notification Service started on port 50052")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
