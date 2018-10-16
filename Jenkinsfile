properties([pipelineTriggers([githubPush()])])

def author_email


pipeline {
    // environment {
    //         // author_email = ""
    // }
    agent { label 'win-appium-slave' }
    
    stages {
        stage ('Checkout'){
            steps{
                script{

                bat 'set > env.txt' 
                for (String i : readFile('env.txt').split("\r?\n")) {
                    println i
                }
                
                bat "echo ${GIT_BRANCH}"
                bat(script:"C:\\Users\\appium\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe parse_git.py >out.txt", returnStdout: true)
                author_email = readFile('out.txt').trim()
                bat "del out.txt"

                
                bat "echo ${author_email}"
                
                bat "git pull origin master"
                

                bat "echo.>out11.txt"
                bat "git add out11.txt"
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

                emailext attachLog: true, body: "${env.JOB_NAME}: ${currentBuild.result} ${JOB_DISPLAY_URL}", compressLog: false, replyTo: "${author_email}", recipientProviders: [developers()], subject: "Jenkins Job Notification: ${JOB_NAME} - Build#${BUILD_NUMBER} ${currentBuild.result}", to: 'elnatn@ravtech.co.il' 
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
