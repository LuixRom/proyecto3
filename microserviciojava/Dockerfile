FROM openjdk:17-jdk-slim

WORKDIR /app
COPY ./src /app/src
COPY ./postgresql.jar /app/postgresql.jar

RUN javac -cp "postgresql.jar" src/*.java

CMD ["java", "-cp", "postgresql.jar:src", "src.app"]
