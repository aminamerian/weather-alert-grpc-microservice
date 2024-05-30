# Weather and Notification Microservices with gRPC

This project consists of two microservices, `weather` and `notification`, which communicate with each other via gRPC. The `weather` microservice acts as a client and sends requests to the `notification` microservice, which acts as a server. The `notification` microservice is responsible for sending notifications to users based on the requests received from the `weather` microservice.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Run the services using Docker](#run-the-services-using-docker)

## Features

- Communication between microservices using gRPC.
- Dummy implementations for weather and notification functionalities.
- Extensible architecture for adding real functionalities in the future.

## Requirements

- Python 3.x
- gRPC Python library
- Docker
- Docker Compose

## Run the services using Docker

1. Clone this repository to your local machine:

    ```bash
    git clone git@github.com:aminamerian/weather-alert-grpc-microservice.git
    ```

2. To run the microservices using Docker, run the following command:

    ```bash
    docker compose up
    ```