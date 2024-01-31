FROM python:3
WORKDIR /app
COPY read.py .
COPY requirments.txt .
RUN pip install -r requirments.txt
CMD [ "python", "./read.py" ]

