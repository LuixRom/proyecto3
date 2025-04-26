FROM openjdk:17-jdk-slim

WORKDIR /app

RUN apt-get update && apt-get install -y wget && \
    wget https://jdbc.postgresql.org/download/postgresql-42.7.1.jar -O postgresql.jar

COPY ./src /app/src

WORKDIR /app/src

RUN javac -cp "../postgresql.jar" *.java

CMD ["java", "-cp", "../postgresql.jar:.", "app"]