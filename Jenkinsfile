pipeline {
    agent any

    environment {
        IMAGE_NAME = "kiyeon24/flask-app-0701"
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        // stage('Checkout') {
        //     steps {
        //         git 'https://github.com/jkyand24/flask-app-0701.git'
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${TAG} ."
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push ${IMAGE_NAME}:${TAG}"
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // 기존 컨테이너 제거 (있다면)
                    sh "docker rm -f flask-app || true"

                    // 새 컨테이너 실행
                    sh "docker run -d --name flask-app -p 4000:4000 ${IMAGE_NAME}:${TAG}"
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}
