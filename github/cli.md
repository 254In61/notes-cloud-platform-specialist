# Install
 $ sudo apt  install -y gh

# Login 

 $ gh auth login

? What account do you want to log into? GitHub.com
The value of the GITHUB_TOKEN environment variable is being used for authentication.
To have GitHub CLI store credentials instead, first clear the value from the environment.
amaseghe@black-panther:~/developer$ 
amaseghe@black-panther:~/developer$ unset GITHUB_TOKEN
amaseghe@black-panther:~/developer$ 
amaseghe@black-panther:~/developer$ gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 130D-E540
Press Enter to open github.com in your browser... 
Opening in existing browser session.
✓ Authentication complete.
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as 254In61

# confirm 

 $ gh auth status
github.com
  ✓ Logged in to github.com account 254In61 (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: gho_************************************
  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'

# operations

- List repos
 $ gh repo list

Showing 30 of 75 repositories in @254In61

NAME                                DESCRIPTION                         INFO     UPDATED             
254In61/notes-cloud-platform-sp...                                      public   about 21 minutes ago
254In61/terraform-configuration...  Configuration code for ec2 depl...  private  about 1 hour ago
254In61/utilities                   A mix of tools that make my lif...  private  about 1 hour ago
254In61/aws-msb-toolkit             Contains scripts to enforce min...  private  about 9 days ago
254In61/terraform-module-aws-ec2    Creates and manages my EC2          private  about 13 days ago
!
!
!

- List only your repos
  $ gh repo list YOUR_USERNAME

  $ gh repo list YOUR_USERNAME --limit 100

  $ gh repo list --limit 100
   
   Showing 55 of 55 repositories in @254In61

  NAME                                                   DESCRIPTION                                              INFO          UPDATED             
254In61/notes-cloud-platform-specialist                                                                         public        about 55 minutes ago
254In61/terraform-configuration-aws-ec2                Configuration code for ec2 deployment                    private       about 1 hour ago
254In61/utilities                                      A mix of tools that make my life easy when doing dev...  private       about 1 hour ago
254In61/aws-msb-toolkit                                Contains scripts to enforce minimum security baselin...  private       about 9 days ago
 

- Limit results
  $ gh repo list YOUR_USERNAME --limit 100

- Show private repos too
  $ gh repo list YOUR_USERNAME --visibility private

- rename repo 
  $ gh repo rename NEW_NAME --repo YOUR_USERNAME/OLD_NAME

- deleting repos ** looks more complex
  $ gh repo delete YOUR_USERNAME/REPO_NAME --yes

  $ gh repo delete 254In61/aws-learning-notes --yes
HTTP 403: Must have admin rights to Repository. (https://api.github.com/repos/254In61/aws-learning-notes)
This API operation needs the "delete_repo" scope. To request it, run:  gh auth refresh -h github.com -s delete_repo

  $ gh auth refresh -h github.com -s delete_repo
? Authenticate Git with your GitHub credentials? Yes

! First copy your one-time code: C87D-A6D6             <=== I copy pasted this one to the Opened browser tab
Press Enter to open github.com in your browser... 
Opening in existing browser session.
✓ Authentication complete.

  ** Things work from here : 

  $ gh repo delete 254In61/aws-learning-notes --yes
✓ Deleted repository 254In61/aws-learning-notes

- Create repo
  $ gh repo create myrepo --private

- Clone a repo
  $ gh repo clone OWNER/REPO
  $ gh repo clone 254In61/ansible-juniper-software-upgrade
   Cloning into 'ansible-juniper-software-upgrade'...