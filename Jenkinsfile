properties([pipelineTriggers([githubPush()])])

pipeline {
    agent { label 'win-appium-slave' }
    stages {
        stage ('Checkout'){
            steps{
                checkout([
            $class: 'GitSCM',
            branches: scm.branches,
            extensions: scm.extensions + [[$class: 'LocalBranch'], [$class: 'WipeWorkspace']],
            userRemoteConfigs: [[credentialsId: 'f6518de0-52e6-4f88-8880-ec7b7216224c', url: 'git@github.com:elnatanst/test-jenkins-git.git']],
            doGenerateSubmoduleConfigurations: false
        ])


        // git branches: [[name: 'refs/head/*']], url: 'git@github.com:elnatanst/test-jenkins-git.git'
            }
    }
        
        stage('pull from master'){
            steps{
                script{

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
