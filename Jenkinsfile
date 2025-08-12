pipeline {
    agent any

    tools {
        jdk 'jdk-17'
        allure 'Allure-CLI'
    }

    environment {
        // Use your python path (set earlier)
        PYTHON = 'C:\\Users\\aravi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                echo ">>> currentBuild BEFORE checkout: ${currentBuild.currentResult}"
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git', changelog: false, poll: false
                echo ">>> currentBuild AFTER checkout: ${currentBuild.currentResult}"
            }
        }

        stage('Install dependencies') {
            steps {
                bat "\"${env.PYTHON}\" -m pip install --upgrade pip"
                bat "\"${env.PYTHON}\" -m pip install pytest allure-pytest selenium pytest-xdist"
                echo ">>> currentBuild AFTER pip install: ${currentBuild.currentResult}"
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // run tests, capture exit code
                    def rc = bat(script: "\"${env.PYTHON}\" -m pytest -n auto test_salesforce.py --alluredir=allure-results", returnStatus: true)
                    echo ">>> pytest exit code: ${rc}"
                    echo ">>> currentBuild AFTER pytest: ${currentBuild.currentResult}"
                }
            }
        }

        stage('Quick check allure-results for failures') {
            steps {
                // quick search for the word failed in result jsons
                bat 'echo === Searching allure-results for "failed" ==='
                bat 'findstr /S /I "failed" allure-results\\*.json || echo NO_FAILED_FOUND'
            }
        }

        stage('Generate Allure report') {
            steps {
                echo ">>> currentBuild BEFORE allure generate: ${currentBuild.currentResult}"
                allure includeProperties: false, results: [[path: 'allure-results']]
                echo ">>> currentBuild AFTER allure generate: ${currentBuild.currentResult}"
            }
        }

        stage('Inspect build actions (debug)') {
            steps {
                script {
                    echo ">>> currentBuild at inspect stage: ${currentBuild.currentResult}"
                    def rb = currentBuild.rawBuild
                    if (rb == null) {
                        echo "rawBuild is null (sandbox restriction?)"
                    } else {
                        // Check for JUnit action
                        def junit = rb.getAction(hudson.tasks.junit.TestResultAction.class)
                        echo "JUnit TestResultAction present: ${junit != null}"
                        if (junit) {
                            echo "  JUnit totals -> total: ${junit.totalCount}, failed: ${junit.failCount}, skipped: ${junit.skipCount}"
                        }

                        // Print list of action class names so we can spot publishers
                        def actions = rb.getActions().collect { it.class.name }.unique().join('\\n')
                        echo "Actions attached to build:\\n${actions}"
                    }
                }
            }
        }

        stage('Archive Allure report') {
            steps {
                archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
                echo ">>> currentBuild AFTER archiveArtifacts: ${currentBuild.currentResult}"
            }
        }
    }

    post {
        always {
            echo "=== POST: currentBuild.currentResult = ${currentBuild.currentResult} ==="
            echo "If build is UNSTABLE, copy the console lines that show:"
            echo "  - pytest exit code"
            echo "  - output of findstr (NO_FAILED_FOUND or matches)"
            echo "  - JUnit totals (if printed)"
            echo "  - Actions attached to build"
        }
    }
}
