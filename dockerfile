# use an official python runtime as the base image
FROM python:3.9-slim

# set the working directory
WORKDIR /reverse_origin_ip

# copy the application files to the container
COPY reverse_origin_ip.py .

# install Flask
RUN pip install flask

# expose the port the app runs on
EXPOSE 80

# define the command to run the application
CMD ["python", "reverse_origin_ip.py"]

