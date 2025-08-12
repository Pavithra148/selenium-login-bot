pipeline {
    agent any

    tools {
        nodejs 'nodejs-18'
        allure 'Allure-CLI'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'npm install'
                    } else {
                        bat 'npm install'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'npx playwright test --reporter=line'
                    } else {
                        bat 'npx playwright test --reporter=line'
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'npx allure generate allure-results --clean -o allure-report'
                    } else {
                        bat 'npx allure generate allure-results --clean -o allure-report'
                    }
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline finished!"
        }
        failure {
            echo "❌ Pipeline failed! Check logs."
        }
    }
}
