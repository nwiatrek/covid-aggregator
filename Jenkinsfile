void dockerCleanupContainer(String container) {
    try {
        sh("docker rm ${container}")
    }
    catch(hudson.AbortException e) {
        echo "Couldn't clean up Docker container"
    }
}

void dockerCleanupImage(String image) {
    try {
        sh("docker rmi ${image}")
    }
    catch(hudson.AbortException e) {
        echo "Couldn't clean up Docker image"
    }
}

void exportPytestResults(String resultsPath = 'results.xml') {
    try {
        junit resultsPath
    }
    catch(hudson.AbortException e) {
        echo "Unit test results are stale, pytest did not run successfully."
    }
}

String getRepoName() {
    return env.GIT_URL.substring(env.GIT_URL.lastIndexOf('/') + 1, env.GIT_URL.length())
}


/**
 * Returns the set of changes for the current build
 * This method should only be called within the context
 * of a Jenkins build.
 *
 * @return the changeset for the current Jenkins build
 */
List<hudson.plugins.git.GitChangeSet> getChangeset() {
    def changeLog = currentBuild.changeSets
    def changes = []
    for (int i = 0; i < changeLog.size(); i++) {
        def entries = changeLog[i].items
        for (int j = 0; j < entries.length; j++) {
            changes << entries[j]
        }
    }

    return changes
}


/**
 * Generates a block of html representing the changeset's information
 * Currently, you can alter this method to change the way changesets are
 * represented
 *
 * @param entry The changeset to retrieve an html representation of
 * @return a string of HTML representing the GitChangeSet
 */
String getHTMLStringForEntry(hudson.plugins.git.GitChangeSet entry) {

    def commitLink = "${env.GIT_URL}/commit/${entry.commitId}"
    String convertedHtmlEntry = """<a href=${commitLink}>${entry.commitId}</a> by ${entry.author} on ${new Date(entry.timestamp)}: ${entry.msg}"""

    return convertedHtmlEntry
}


/**
 * Gets a full block of html representing an entire set of changes
 *
 * @param changes A list of git changes to retrieve an HTML representation of
 * @return A block of HTML representing a list of changes
 */
String getHTMLBlockForChangeset(List<hudson.plugins.git.GitChangeSet> changes) {

    def body = ""

    for (int i = 0; i < changes.size(); i++) {
        body += "<li>${getHTMLStringForEntry(changes[i])}</li>"
    }

    body = "<ol>${body}</ol>"

    return body
}


/**
 * Sends an email as specified
 *
 * @param subject The subject of the email
 * @param body The email's body
 * @param recipient The intended recipient of the email
 */
void sendEmail(String subject, String body, String recipient) {
    emailext (to: recipient,
        subject: subject,
        body: body,
        mimeType: "text/html")
}


/**
 * Builds out a standard email body for a deployment email
 *
 * @param branch the branch that has been deployed to
 * @return A block of HTML representing the changes that have been deployed
 */
String constructDeploymentEmailBody(String branch) {
    def body = """<p>The following changes were made to ${branch} in <a href="${env.GIT_URL}">${getRepoName()}</a>:</p>"""

    def changes = getChangeset()
    body += getHTMLBlockForChangeset(changes)

    def link = "${env.GIT_URL}"
    link += "/commit/${env.GIT_COMMIT}"

    body += "<p>Please see ${link} for more details!</p>"

    return body
}



/**
 * Builds out a standard email body for a failed deployment
 *
 * @param branch The branch that was unsuccessfully deployed to
 * @return String of HTML representing which changes were unsucessfully deployed
 */
String constructDeploymentFailureEmailBody(String branch) {
    def body = """<p style="color:red">An error occurred when attempting to deploy ${branch} in <a href="${env.GIT_URL}">${getRepoName()}</a>, the list of changes attempted to deploy can be found below:</p>"""
    body += getChangeset()

    def link = "${env.GIT_URL}"

    body += """<p>Details about the failed build can be found <a href="${env.BUILD_URL}">here</a></p>"""

    return body
}


/**
 * Sends a notification about deployments in the specified manner
 *
 * @param deployStageStatus The status of the deploy stage (actions taken on "SUCCESS" or "FAILURE")
 * @param emailRecipient The email address that notifications about the deployment email should be sent to
 */
void sendDeploymentNotification(String deployStageStatus, String emailRecipient) {
    def emailBody = ""
    def subject = "Deployment of ${getRepoName()}"

    if (deployStageStatus == 'SUCCESS') {
        emailBody = constructDeploymentEmailBody(env.GIT_BRANCH)
    } else if (deployStageStatus == 'FAILURE') {
        emailBody = constructDeploymentFailureEmailBody(env.GIT_BRANCH)
    }

    sendEmail(subject, emailBody, emailRecipient)
}

void loadProperties() {
    echo 'Reading properties file'
    props = readProperties file: 'env.properties'
}

void exportUnitTests() {
    echo 'Exporting Tests'
    sh("docker cp covid_aggregator_unittests_${env.BUILD_ID}:/opt/covid-aggregator/results.xml results.xml")
    exportPytestResults()
}

void dockerCleanup() {
    echo 'Cleaning up Docker'
    dockerCleanupImage("covid_aggregator:${env.BUILD_ID}")
    dockerCleanupContainer("covid_aggregator_unittests_${env.BUILD_ID}")
    dockerCleanupImage("covid_aggregator_unittests:${env.BUILD_ID}")
}

// main pipeline build set
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
                        sendDeploymentNotification('SUCCESS', props.DEFAULT_EMAIL_RECIPIENT)
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
                        sendDeploymentNotification('SUCCESS', props.DEFAULT_EMAIL_RECIPIENT)
                }
            }
            post {
                failure {
                    script {
                        sendDeploymentNotification('FAILURE', props.DEFAULT_EMAIL_RECIPIENT)
                    }
                }
                success {
                    script {
                        sendDeploymentNotification('SUCCESS', props.DEFAULT_EMAIL_RECIPIENT)
                    }
                }
            }
        }

        stage('End') {
            steps {
                echo 'test'
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