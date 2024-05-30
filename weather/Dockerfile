FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY weather/ /service/weather/
WORKDIR /service/weather
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/notification.proto

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]