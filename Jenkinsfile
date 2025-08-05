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
                call "selenium Practice\\.venv\\Scripts\\activate.bat"
                pytest --html=reports/Salesforce.html test_salesforce.py
                '''
            }
        }

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', onlyIfSuccessful: true
            }
        }
    }

    post {
        always {
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'Salesforce.html',
                reportName: 'Test Report',
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }
    }
}
