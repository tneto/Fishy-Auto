FROM postgres

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv libpq-dev

# Create a virtual environment and install psycopg2-binary in it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN /opt/venv/bin/python3 -m pip install --upgrade pip
RUN /opt/venv/bin/python3 -m pip install psycopg2-binary
