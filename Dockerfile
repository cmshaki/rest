FROM python

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements file and install
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy django app to container volume
COPY ./backend/cfehome /app

# Set up work directory
WORKDIR /app

# Copying entry point file and setting it up
COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]