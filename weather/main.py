import os
from fastapi import FastAPI, HTTPException
import grpc
from grpc import StatusCode
import notification_pb2_grpc
from notification_pb2 import WeatherAlert

app = FastAPI()

notification_host = os.getenv("NOTIFICATION_HOST", "localhost")
channel = grpc.insecure_channel(f"{notification_host}:50052")
user_notification_client = notification_pb2_grpc.UserNotificationServiceStub(channel)


def send_weather_alert(location, temperature, humidity, wind_speed):
    alert = WeatherAlert(
        location=location,
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
    )
    try:
        return user_notification_client.SendWeatherAlert(alert)
    except grpc.RpcError as e:
        if e.code() == StatusCode.UNAVAILABLE:
            raise HTTPException(
                status_code=503, detail="Notification service unavailable"
            )
        else:
            raise HTTPException(status_code=500, detail="Internal server error")


@app.post("/notify")
def notify():
    response = send_weather_alert(
        location="New York", temperature=25, humidity=80, wind_speed=10
    )
    if response.success:
        return {"message": response.message}
    else:
        raise HTTPException(status_code=500, detail="Failed to send weather alert")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
