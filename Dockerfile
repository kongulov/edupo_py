FROM python:3.10

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code
ENV DEBUG False

# Copy in your requirements filee
ADD requirements.txt /requirements.txt

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN pip install virtualenvwrapper && \
    python3 -m venv /venv && \
    /venv/bin/pip install -U pip && \
    /venv/bin/pip install --no-cache-dir -r /requirements.txt

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

# uWSGI will listen on this port
EXPOSE 8000

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi

# Start uWSGI
CMD [ "/venv/bin/uwsgi", "--ini", "/code/uwsgi.ini"]


