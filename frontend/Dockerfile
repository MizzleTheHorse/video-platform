FROM python

ENV PYTHONUNBUFFERED=1

RUN mkdir /frontend

COPY . /frontend

WORKDIR /frontend

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

#uninstall broken package
RUN python -m pip install markupsafe==2.0.1

#RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
#
#           --grpc_python_out=. ../protobufs/user_service.proto

RUN python3 -m grpc_tools.protoc -I protobufs --python_out=. \
           --grpc_python_out=. protobufs/user_service.proto


RUN python3 -m grpc_tools.protoc -I protobufs --python_out=. \
           --grpc_python_out=. protobufs/video_service.proto


EXPOSE 5000

ENV FLASK_APP=__init__.py

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]

#CMD [ "flask", "--app" , ".", "run"]