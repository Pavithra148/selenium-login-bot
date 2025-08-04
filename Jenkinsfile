pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Pavithra148/selenium-login-bot.git'
            }
        }

        stage('Set up Python & Run Tests') {
            steps {
                bat '''
               call "selenium Practice\\.venv\\Scripts\\activate.bat"
                python Salesforce.py
                '''
            }
        }

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', onlyIfSuccessful: true
            }
        }
    }
}
