@Library('Utils') _

void loadProperties() {
    echo 'Reading properties file'
    props = readProperties file: 'env.properties'
}

void exportUnitTests() {
    echo 'Exporting Tests'
    sh("docker cp covid_aggregator_unittests_${env.BUILD_ID}:/opt/job-manager/results.xml results.xml")
    utils.exportPytestResults()
}

void dockerCleanup() {
    echo 'Cleaning up Docker'
    utils.dockerCleanupImage("covid_aggregator:${env.BUILD_ID}")
    utils.dockerCleanupContainer("covid_aggregator_unittests_${env.BUILD_ID}")
    utils.dockerCleanupImage("covid_aggregator_unittests:${env.BUILD_ID}")
}

pipeline {

    agent {
        node {
            label "${env.AGENT_LABEL}" // Executes the pipeline on agents with this label
        }
    }

    stages {

        stage('Start') {
            steps {
                echo 'Starting build'
                loadProperties()
                script {
                        deploy.sendDeploymentNotification('SUCCESS', props.DEFAULT_EMAIL_RECIPIENT)
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh("docker build -t covid_aggregator:${env.BUILD_ID} .")
                }
            }
        }

        stage('Build Unit Tests') {
            steps {
                script {
                    docker.build("covid_aggregator_unittests:${env.BUILD_ID}", "-f tests/tests.Dockerfile .")
                    sh("docker create --name covid_aggregator_unittests_${env.BUILD_ID} --network none covid_aggregator_unittests:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Start the container attached
                sh("docker start -a covid_aggregator_unittests_${env.BUILD_ID}")
            }
        }

        stage('Deploy') {
            when {
                allOf {
                    expression {
                        env.GIT_BRANCH == "origin/master"
                    }

                    expression {
                        currentBuild.getBuildCauses("com.cloudbees.jenkins.GitHubPushCause").size() > 0
                    }
                }
            }
            steps {
                script {
                        deploy.sendDeploymentNotification('SUCCESS', props.DEFAULT_EMAIL_RECIPIENT)
                }
            }
            post {
                failure {
                    script {
                        deploy.sendDeploymentNotification('FAILURE', props.DEFAULT_EMAIL_RECIPIENT)
                    }
                }
                success {
                    script {
                        deploy.sendDeploymentNotification('SUCCESS', props.DEFAULT_EMAIL_RECIPIENT)
                    }
                }
            }
        }

        stage('End') {
            steps {
                echo 'Ending build'
            }
        }

    }

    post { // These steps are run after all the stages

        aborted { // Will only run if the run was aborted, usually manual
            echo 'Aborted'
        }

        always {
            exportUnitTests()
            dockerCleanup()
        }

        failure { // Only runs if the run has failed
            echo 'Failure'
        }

        success { // Only runs if the run has succeeded
            echo 'Success'
        }

        unstable { // Only runs if the run is unstable
            echo 'Unstable'
        }

    }

}