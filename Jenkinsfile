properties([pipelineTriggers([githubPush()])])




pipeline {
    agent { label 'win-appium-slave' }
    stages {
        stage ('Checkout'){
            steps{
                script
                bat "git branch"
                bat "git checkout master"
                bat "git branch"
                bat "echo.>out.txt"
                bat "git add out.txt"
                bat "git commit -m\"test10\""
                def GIT_COMMIT_EMAIL = bat (
                script: 'git --no-pager show -s --format=\'%ae\'',
                returnStdout: true).trim()
                echo "Git committer email: ${GIT_COMMIT_EMAIL}"
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
