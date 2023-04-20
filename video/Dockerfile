FROM python

ENV PYTHONUNBUFFERED=1

RUN mkdir /system

COPY protobufs/ /system/protobufs/
COPY service/ /system/service/
COPY requirements.txt/ /system/

WORKDIR /system

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I protobufs --python_out=/system/service/ \

           --grpc_python_out=/system/service/ protobufs/video_service.proto


EXPOSE 50051


ENTRYPOINT ["python", "service/server.py"]