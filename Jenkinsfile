pipeline {
    agent any

    triggers {
        githubPush()
    }

    tools {
        jdk 'jdk-17'
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
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git', changelog: false, poll: false
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest allure-pytest selenium'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        def exitCode = bat(script: 'python -m pytest test_salesforce.py --alluredir=allure-results', returnStatus: true)
                        if (exitCode != 0) {
                            error "Tests failed with exit code ${exitCode}"
                        }
                    }
                }
            }
        }

        stage('Debug Workspace') {
            steps {
                bat 'dir /s'
            }
        }

        stage('Debug Allure Results Folder') {
            steps {
                bat 'dir allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }

        stage('Debug Allure Report Folder') {
            steps {
                bat 'dir allure-report'
            }
        }

        stage('Archive Allure Report') {
            steps {
                archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo "Build result at end: ${currentBuild.currentResult}"
        }
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
        unstable {
            echo 'Pipeline is unstable'
        }
    }
}
