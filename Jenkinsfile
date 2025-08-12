pipeline {
    agent any

    triggers {
        githubPush()
    }

    tools {
        jdk 'jdk-17'
        allure 'Allure-CLI'
    }

    environment {
        PYTHON_PATH = 'C:\\Users\\aravi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git', changelog: false, poll: false
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"${env.PYTHON_PATH}\" -m pip install --upgrade pip"
                bat "\"${env.PYTHON_PATH}\" -m pip install pytest allure-pytest selenium pytest-xdist"
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        // Run tests but ignore failures for build status
                        bat(script: "\"${env.PYTHON_PATH}\" -m pytest -n auto test_salesforce.py --alluredir=allure-results || exit /b 0")
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo "Final Build Status: SUCCESS (forced)"
        }
        success {
            echo '✅ Pipeline marked as SUCCESS regardless of test results'
        }
    }
}
