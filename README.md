# Weather and Notification Microservices with gRPC

This project consists of two microservices, `weather` and `notification`, which communicate with each other via gRPC. The `weather` microservice acts as a client and sends requests to the `notification` microservice, which acts as a server. The `notification` microservice is responsible for sending notifications to users based on the requests received from the `weather` microservice.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Features

- Communication between microservices using gRPC.
- Dummy implementations for weather and notification functionalities.
- Extensible architecture for adding real functionalities in the future.

## Requirements

- Python 3.x
- gRPC Python library

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone git@github.com:aminamerian/weather-alert-grpc-microservice.git
    ```

2. Install the required dependencies for weather service:

    ```bash
    cd weather
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. Install the required dependencies for notification service:

    ```bash
    cd notification
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

1. Start the `notification` microservice:

    ```bash
    cd notification
    source venv/bin/activate
    python notification.py
    ```
    The output should be similar to the following:

    ```bash
    User Notification Service started on port 50052
    ```

2. Start the `weather` microservice:

    ```bash
    cd weather
    source venv/bin/activate
    python weather.py
    ```