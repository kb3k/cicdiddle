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
