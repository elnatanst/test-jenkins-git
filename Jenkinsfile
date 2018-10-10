pipeline {
    agent { label 'win-appium-slave' }
    stages {
        
        stage('pull from master'){
            steps{
                script{
                    
                    bat "%ANDROID_HOME%/tools/emulator -avd Pixel_XL_API_26 -no-window"
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
            // sh 'mv app/build/outputs/apk/debug/app-debug.apk app/build/outputs/apk/debug/Build-${BUILD_NUMBER}-debug.apk || true'
            // sh 'mv app/build/outputs/apk/release/app-release-unsigned.apk app/build/outputs/apk/debug/Build-${BUILD_NUMBER}-release.apk || true'
            // script{
            //         if(env.RUN_LINT_TEST == 'true'){
            //             androidLint failedNewHigh: '0'
            //         }
            // }
            // archiveArtifacts allowEmptyArchive: true, artifacts: '*/**/*.apk'
            // step([$class           : 'Mailer',
            //       recipients       : "admin@ravtech.co.il",
            //       sendToIndividuals: false])
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
