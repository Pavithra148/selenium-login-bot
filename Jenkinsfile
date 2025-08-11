pipeline {
    agent any

    triggers {
        githubPush() // Trigger on GitHub push webhook
    }

    tools {
        git 'TestG'           // Your Git tool name configured in Jenkins
        jdk 'jdk-17'          // Your JDK tool name
        allure 'Allure-CLI'   // Your Allure tool name
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
                    // Run pytest with allure results and junit xml output
                    def exitCode = bat(
                        script: 'python -m pytest test_salesforce.py --alluredir=allure-results --junitxml=reports/results.xml',
                        returnStatus: true
                    )
                    if (exitCode != 0) {
                        error "Tests failed with exit code ${exitCode}"
                    }
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'reports/results.xml'
            }
        }

        stage('Debug Allure Results') {
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
            script {
                def testResult = currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class)
                if (testResult != null) {
                    echo "Total tests: ${testResult.totalCount}, Failed: ${testResult.failCount}, Skipped: ${testResult.skipCount}"
                } else {
                    echo "No JUnit test results found."
                }
            }
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
