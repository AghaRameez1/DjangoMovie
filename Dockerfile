FROM python:3.9 as backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project


COPY . /project/


RUN pip install -r requirements.txt

RUN chmod +x /project/entrypoint.sh
EXPOSE 8000
ENTRYPOINT  [ "/project/entrypoint.sh" ]


# CMD [ "python", "manage.py" ,"runserver","0.0.0.0:8000" ]
# copy entrypoint.sh
# RUN sed -i 's/\r$//g' /project/entrypoint.sh

# CMD ["gunicorn", "djangoProject.wsgi:application", "--bind 0.0.0.0:8000"]