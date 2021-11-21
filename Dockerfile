FROM python:3.9

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=apps
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run","--host", "0.0.0.0"]