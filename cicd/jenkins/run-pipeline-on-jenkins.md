# Option 1 : Directly from Jenkins server
1. Log into your Jenkins server and install Ansible

2. Give Jenkins permission to run Ansible

3. Place your Ansible project where Jenkins can access it.
   - Could be inside /var/lib/jenkins/workspace/ (after the job is created) or in a Git repo so Jenkins clones it.
   - Best practice: store your Ansible playbooks in Git → Jenkins pulls them → Jenkins runs them.

4. Install required Jenkins plugins

Go to:

Manage Jenkins → Plugins → Available plugins

Install:

✅ Git Plugin
✅ SSH Build Agents (optional)
✅ AnsiColor (for coloured Ansible output)
✅ Credentials Binding Plugin

5. Add SSH credentials in Jenkins

Go to:

Manage Jenkins → Credentials → System → Global Credentials

Add:

Kind: SSH Username with private key

Username: jenkins

Private Key: paste /var/lib/jenkins/.ssh/id_ed25519

This will be used to connect to your Ansible hosts.

6. Create a Jenkins Pipeline job

New Item → Pipeline

Scroll down to Pipeline Script and paste something like this:

pipeline {
    agent any

    environment {
        ANSIBLE_FORCE_COLOR = 'true'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR-REPO/ansible.git'
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                ansiColor('xterm') {
                    sh """
                    ansible-playbook -i inventories/production site.yml \
                        --ssh-extra-args='-o StrictHostKeyChecking=no'
                    """
                }
            }
        }
    }
}

✅ 7. Run your first pipeline

Click Build Now → Jenkins will pull your repo and run:

ansible-playbook site.yml

# Option 2: Run Ansible inside a Docker container in Jenkins

This method keeps Jenkins clean, ensures consistent Ansible versions, and works with both Freestyle and Pipeline jobs.

✅ 1. Create an Ansible Docker image