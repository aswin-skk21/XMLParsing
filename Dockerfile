FROM python:3.12

WORKDIR /src

COPY xml_parser.py .

CMD ["python", "main.py"]