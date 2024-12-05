pipeline {
    agent any
    triggers {
    githubPush()
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ItayGo/cicd.git', credentialsId: 'github-credentials'
            }
        }
    }
}

