# Install .NET on Ubuntu
1. Update packages
sudo apt-get update
sudo apt-get install -y wget apt-transport-https

2. Add Microsoft package repo
wget https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update

3. Install .NET SDK (for development)
sudo apt-get install -y dotnet-sdk-8.0

4. Verify installation
dotnet --version

5. Create & run a test app
mkdir hello-dotnet && cd hello-dotnet
dotnet new console -o app
cd app
dotnet run

You should see:

Hello, World!
