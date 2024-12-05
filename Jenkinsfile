pipeline {
    agent any
    triggers {
    githubPush()
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ItayGo/cicd.git', credentialsId: 'github-credentials'
            }
        }
    }
}

