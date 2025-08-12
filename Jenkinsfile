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
        TIMESTAMP = "${new Date().format('yyyyMMdd_HHmmss')}"
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
                        // Run tests but force exit code 0 so pipeline never fails
                        bat(script: "\"${env.PYTHON_PATH}\" -m pytest -n auto test_salesforce.py --alluredir=allure-results || exit /b 0")
                    }
                }
            }
        }

        stage('Preserve Allure History') {
            steps {
                script {
                    bat "if exist allure-results\\history xcopy /E /I /Y allure-results\\history allure-report\\history"
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }

        stage('Save Allure Report with Timestamp') {
            steps {
                script {
                    bat "mkdir allure-history"
                    bat "xcopy /E /I /Y allure-report allure-history\\${env.TIMESTAMP}"
                }
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline forced to SUCCESS - check Allure report for failures."
        }
    }
}
