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
                        // Capture exit code but don't fail immediately
                        def exitCode = bat(script: "\"${env.PYTHON_PATH}\" -m pytest -n auto test_salesforce.py --alluredir=allure-results", returnStatus: true)
                        
                        // Decide build status based on exit code
                        if (exitCode != 0) {
                            currentBuild.result = 'FAILURE'
                            error "Tests failed with exit code ${exitCode}"
                        }
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
            echo "Final Build Status: ${currentBuild.result}"
        }
        failure {
            echo '❌ Pipeline failed due to test errors'
        }
        success {
            echo '✅ Pipeline passed without issues'
        }
    }
}
