pipeline {
    agent any

    environment {
        VENV_DIR = 'venv/Scripts'
        REPORT_FILE = 'report.html'
        DEVICE_NAME = 'emulator-5556'
        PLATFORM_NAME = 'Android'
        APP_PATH = 'C:/Users/nmaheshw/app/mda-2.2.0-25.apk'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/CGNeeluMaheshwari/appium_practice_project.git', branch: 'master'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Start Appium Server') {
            steps {
                bat '''
                    echo Starting Appium server...
                    start /B appium > appium.log 2>&1
                    timeout /T 10
                '''
            }
        }

        stage('Keep System Awake') {
            steps {
                bat '''
                    powershell -command "while ($true) { [System.Windows.Forms.SendKeys]::SendWait('{NUMLOCK}'); Start-Sleep -Seconds 300 }" > keepawake.log 2>&1
                '''
            }
        }

        stage('Verify Device Connection') {
            steps {
                bat '''
                    echo Checking connected devices...
                    adb devices
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest tests/ --html=%REPORT_FILE% --self-contained-html -n auto
                '''
            }
        }

        stage('Stop Appium Server') {
            steps {
                bat '''
                    echo Stopping Appium server...
                    taskkill /F /IM node.exe
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: "${env.REPORT_FILE}",
                    reportName: 'Test Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'rmdir /S /Q venv'
        }
        failure {
            echo 'Build failed. Check logs and test report for details.'
        }
    }
}
