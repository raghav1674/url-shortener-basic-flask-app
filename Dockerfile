FROM raghav1674/arthflaskminimal:v1 

ENV FLASK_APP=urlshorten

ENV FLASK_ENV=development

RUN mkdir /flask-app

WORKDIR flask-app

RUN git clone https://github.com/raghav1674/url-shortener-basic-flask-app.git  /flask-app 

COPY ./main.py /flask-app/

ENTRYPOINT ["python3"]

CMD ["/flask-app/main.py","--host='0.0.0.0'"]

EXPOSE 5000

