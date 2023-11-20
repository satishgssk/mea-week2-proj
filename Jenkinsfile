pipeline {
    agent any
    environment {
        PORT = "8000"
        MYSQL_ROOT_PASSWORD = credentials("MYSQL_ROOT_PASSWORD")
    }
    stages {
        stage('Build') {
            steps {
                sh '''
                docker build -t agray998/lbg:${BUILD_NUMBER} --build-arg PORT=${PORT} .
                docker tag agray998/lbg:${BUILD_NUMBER} agray998/lbg:latest
                docker build -t agray998/lbg-mysql:${BUILD_NUMBER} db
                docker tag agray998/lbg-mysql:${BUILD_NUMBER} agray998/lbg-mysql:latest
                docker push agray998/lbg:${BUILD_NUMBER}
                docker push agray998/lbg:latest
                docker push agray998/lbg-mysql:${BUILD_NUMBER}
                docker push agray998/lbg-mysql:latest
                docker rmi agray998/lbg:${BUILD_NUMBER}
                docker rmi agray998/lbg:latest
                docker rmi agray998/lbg-mysql:${BUILD_NUMBER}
                docker rmi agray998/lbg-mysql:latest
                '''
           }
        }
        stage("generate nginx.conf") {
            steps {
                sh '''
                cat - > nginx.conf <<EOF
                events {}
                http {
                    server {
                        listen 80;
                        location / {
                            proxy_pass http://lbg-api:${PORT};
                        }
                    }
                }
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                scp nginx.conf jenkins@adam-deploy:/home/jenkins/nginx.conf
                ssh jenkins@adam-deploy <<EOF
                export PORT=${PORT}
                export VERSION=${BUILD_NUMBER}
                export MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
                docker stop lbg-api && echo "stopped" || echo "not running"
                docker rm lbg-api && echo "removed" || echo "already removed"
                docker stop nginx && echo "stopped" || echo "not running"
                docker rm nginx && echo "removed" || echo "already removed"
                docker stop mysql && echo "stopped" || echo "not running"
                docker rm mysql && echo "removed" || echo "already removed"
                docker network inspect proj && echo "network exists" || docker network create proj
                docker volume inspect proj-vol && echo "volume exists" || docker volume create proj-vol
                docker pull agray998/lbg
                docker pull agray998/lbg-mysql
                docker run -d -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} --network proj --name mysql -v proj-vol:/var/lib/mysql agray998/lbg-mysql
                docker run -d -e PORT=${PORT} -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} --name lbg-api --network proj agray998/lbg
                docker run -d -p 80:80 --name nginx --network proj --mount type=bind,source=/home/jenkins/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine
                '''
            }
        }
    }
}
