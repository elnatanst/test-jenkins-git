pipeline {
    agent { label 'win-appium-slave' }
    stages {
        
        stage('pull from master'){
            steps{
                script{
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

        stage('Android lint') {
            steps {
                script{
                    if(env.RUN_LINT_TEST == 'true'){
                bat '''
            gradlew lint

            '''
                    }
                }
            }
        }
        stage('Android sonarqube') {
            steps {
                script{
                    if(env.RUN_SONARQUBE == 'true'){
                bat '''
            
            gradlew sonarqube

            '''
                    }
                }
            }
        }
        stage('Compile Debug apk') {
            steps {
                script{
                    if(env.MAKE_DEBUG_APK == 'true'){
                bat '''
            
            gradlew assembleDebug
            '''
                    }
                }
            }
        }
        stage('Compile Release apk') {
            steps {
                script{
                    if(env.MAKE_RELEASE_APK == 'true'){
                        
                        
                bat '''
            
            gradlew assembleRelease
            '''
                    }
                }
            }
        }
        
        stage('Firebase TestLab') {
            steps {
                script{
                    if(env.FIREBASE_TEST == 'true'){
                        sh '''
                        cd jenkins
                        chmod +x firebase_test_command.sh
                        ./firebase_test_command.sh
                        cd ..
                        
                        '''
                    }
                }
            }
        }

        stage('publish to nexus'){
            steps{
                script{
                       if(env.PUBLISH_TO_NEXUS == 'true'){
                           
                           
                            def app_version = bat(script: '/usr/bin/python3 jenkins/get_version_from_apk.py -file=app/build/outputs/apk/debug/app-debug.apk',returnStdout: true)
                            bat "echo ${app_version}"
                            bat(script: "/usr/bin/python3 jenkins/nexus_archive_artifacts.py --file=app/build/outputs/apk/debug/app-debug.apk --artId=${NEXUS_GROUPID}-debug --v=${app_version}")
                            bat(script: "/usr/bin/python3 jenkins/nexus_archive_artifacts.py --file=app/build/outputs/apk/release/app-release-unsigned.apk --artId=${NEXUS_GROUPID}-release --v=${app_version}")
                            

                       } 

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
