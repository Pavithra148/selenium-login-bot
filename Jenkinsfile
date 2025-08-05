pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Pavithra148/selenium-login-bot.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install --user -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'pytest --html=report.html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
