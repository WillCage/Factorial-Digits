FROM python:3

COPY /factorial_digits /
COPY /tests /

RUN pip install numpy

ENTRYPOINT ["python", "main.py"]

CMD ["0"]