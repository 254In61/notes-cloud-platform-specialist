# overview
- Having Jenkins CI/CD skillset as my 2nd one after GitHub Actions

# install Jenkins Server

✅ 1. Install Java (required)

Jenkins requires Java 17+:

sudo apt update
sudo apt install fontconfig openjdk-17-jre -y

✅ 2. Add the Jenkins repository key
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

✅ 3. Add the Jenkins APT source list
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

✅ 4. Install Jenkins
sudo apt update
sudo apt install jenkins -y

✅ 5. Start and enable Jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

✅ 6. Open the firewall (if UFW is enabled)
sudo ufw allow 8080
sudo ufw reload

✅ 7. Retrieve the initial admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword


Copy that into the setup wizard in the browser.

# Check status

 - Check systemctl status

 $ systemctl status jenkins

 - Check configuration files :

   Main config : $ less /var/lib/jenkins/config.xml

   Jobs: $ ls /var/lib/jenkins/jobs/


 
# When running

- You want consisteny across runs and a Jenkins server that is clean.

- You don't install stuff on the server host, but you use images to run your runs, keeping the Jenkins host neutral and clean.


# Setting up on your github repo. 

1. Have a Jenkinsfile written in Groovy in your repo.

2. Go to your Jenkins and configure a pipeline to run. 
   - Ensure has credentials for the VCS e.g GitHub.
   - If you are running on a docker image, as you should, ensure Jenkins has credentials to the image repository.
   - Have is as a GitHook for SCM monitoring?
   - Pipeline just runs from there!.. :) :)