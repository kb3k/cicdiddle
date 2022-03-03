FROM python:3.7-slim

ENV FLASK_APP=app
ENV FLASK_ENV=production
RUN echo "#!/bin/bash\n" > /startscript.sh
RUN echo "mkdir github\n" >> /startscript.sh
RUN echo "cd github\n" >> /startscript.sh
RUN echo "git clone \$github\n" >> /startscript.sh
RUN echo "cd *\n" >> /startscript.sh
RUN echo "make dockertest\n" >> /startscript.sh

RUN chmod +x /startscript.sh

CMD /startscript.sh

# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /
RUN pip install -r requirements.txt
# Set the WORKDIR to be the folder
COPY . /app

# Expose port 5000
EXPOSE 5000
ENV PORT 5000

WORKDIR /app

# concurrency is a currency
CMD exec gunicorn --bind :$PORT app:app --workers 1 --threads 1 --timeout 60
