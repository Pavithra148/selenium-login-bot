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
                python -m venv venv
                venv\Scripts\Activate.ps1
                pip install --upgrade pip
                pip install selenium HtmlTestRunner
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
