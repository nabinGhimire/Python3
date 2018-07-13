
## ======================================================================================
## Setting Up Python 3
## ======================================================================================

#Ubuntu 16.04 ships with both Python 3 and Python 2 pre-installed.
sudo apt-get update
sudo apt-get -y upgrade

#Check installed python version
python3 -V

#Install pip to manage software packages for Python
sudo apt-get install -y python3-pip

# Install few more packages and development tools to ensure that we have a robust set-up for our programming environment
sudo apt-get install build-essential libssl-dev libffi-dev python-dev

## ======================================================================================
## Setting Up a Virtual Environment
## ======================================================================================

#We need to first install the venv module, part of the standard Python 3 library, so that we can create virtual environments
sudo apt-get install -y python3-venv

# Let’s choose which directory we would like to put our Python programming environments in
mkdir environments
cd environments

#create an environment
python3 -m venv my_env

#Check the contains oof the my_env directory
ls my_env

#To use this environment, you need to activate it
source my_env/bin/activate

# shows different python things already installed
pip freeze
