pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git'
            }
        }

        stage('Set up Python & Run Tests') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install --upgrade pip
                pip install selenium pytest pytest-html
                pytest --html=reports/Salesforce.html test_salesforce.py
                '''
            }
        }

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', onlyIfSuccessful: true
                publishHTML (target: [
                    reportDir: 'reports',
                    reportFiles: 'Salesforce.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
}
