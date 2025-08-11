pipeline {
    agent any

    triggers {
        githubPush() // Trigger on GitHub push webhook
    }

    tools {
        git 'TestG'             // Your Git tool name configured in Jenkins
        jdk 'jdk-17'            // Your JDK name configured in Jenkins
        allure 'Allure-CLI'     // Your Allure CLI tool configured in Jenkins
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
                    def exitCode = bat(script: 'python -m pytest test_salesforce.py --alluredir=allure-results', returnStatus: true)
                    if (exitCode != 0) {
                        error "Tests failed with exit code ${exitCode}"
                    }
                }
            }
        }

        stage('Debug Workspace') {
            steps {
                echo "Listing workspace files..."
                bat 'dir /s'
            }
        }

        stage('Debug Allure Results Folder') {
            steps {
                echo "Listing allure-results folder contents..."
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
                echo "Listing allure-report folder contents..."
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
