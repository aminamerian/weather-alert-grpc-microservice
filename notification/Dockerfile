FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY notification/ /service/notification/
WORKDIR /service/notification
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/notification.proto

ENTRYPOINT [ "python", "notification.py" ]