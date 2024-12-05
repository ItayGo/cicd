pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ItayGo/cicd.git', credentialsId: 'github-credentials'
            }
        }
    }
}

