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

        stage('Verify Workspace') {
            steps {
                bat 'dir /s'
            }
        }

        stage('Run Tests with Debug') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        // Fail fast on first test failure, show detailed errors
                        def exitCode = bat(script: 'python -m pytest test_salesforce.py --maxfail=1 --disable-warnings -v --alluredir=allure-results', returnStatus: true)
                        
                        echo "Pytest exit code: ${exitCode}"
                        
                        if (exitCode != 0) {
                            error "Tests failed. Check above logs for exact reason."
                        }
                    }
                }
            }
        }

        stage('Check Allure Results') {
            steps {
                bat 'dir allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }

        stage('Check Allure Report') {
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
            echo "Build finished with status: ${currentBuild.currentResult}"
        }
        success {
            echo '✅ Pipeline succeeded'
        }
        failure {
            echo '❌ Pipeline failed — see logs above for details'
        }
        unstable {
            echo '⚠️ Pipeline unstable — likely test failures'
        }
    }
}
