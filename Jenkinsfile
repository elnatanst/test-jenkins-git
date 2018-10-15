properties([pipelineTriggers([githubPush()])])




pipeline {
    agent { label 'win-appium-slave' }
    environment {
            author_email = "admin"
    }
    stages {
        stage ('Checkout'){
            steps{
                script{
                bat "git rev-parse --abbrev-ref HEAD"
                bat "git branch"
                def out = bat(script:"C:\\Users\\appium\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe parse_git.py", returnStdout: true)
                sleep(10)
                
                bat "echo ${env.out}"
                
                
                bat "git pull origin master"
                bat "git checkout master"

                // bat "git status"
                // bat "echo.>out11.txt"
                // bat "git add out11.txt"
                // bat "git add out111.txt"
                bat "git commit -m\"test10\""
                
                // echo "Git committer email: ${env.author_email}"
                bat "git push origin master"
            }
            }
    }
        
        stage('pull from master'){
            steps{
                script{
                    bat "git branch"
                    bat "C:\\Users\\appium\\AppData\\Local\\Android\\Sdk\\tools\\emulator -avd Pixel_XL_API_26 -no-window"
                    bat "adb devices"



                    bat '''
                                git fetch origin
                                git branch
                                git checkout -b test
                                git pull origin master
                                echo.> test.txt
                                git add test.txt
                                git commit -m "test push"
                                git push test
                                '''
                    
            }
            }

        }


    }
    post {
        always {
            script{

                emailext attachLog: true, body: "${env.JOB_NAME}: ${currentBuild.result} ${BUILD_URL}", compressLog: false, replyTo: 'admin@ravtech.co.il', recipientProviders: [developers()], subject: "Jenkins Job Notification: ${JOB_NAME} - Build#${BUILD_NUMBER} ${currentBuild.result}", to: 'elnatn@ravtech.co.il' 
            }
            
            
            deleteDir()
        }
        success {

            script{
                    if(env.NAME_OF_GITLAB_COMMIT_TO_UPDATE != null){   
                        updateGitlabCommitStatus name: env.NAME_OF_GITLAB_COMMIT_TO_UPDATE, state: 'success'
                    }
            }
        }

        failure {
            script{
                    if(env.NAME_OF_GITLAB_COMMIT_TO_UPDATE != null){
                        updateGitlabCommitStatus name: env.NAME_OF_GITLAB_COMMIT_TO_UPDATE, state: 'failed'
                    }
            }
        }
    }
}
