=================
ACM Website at KU
=================

This repository is simply a skeleton of a Django project for the University of Kansas ACM Chapter website. Main complications witInstall of any Python system is recommended in a virtual enviroment. Below is a rough idea of how to set this up on EECS servers. Difficulties in the code contained here invovles getting the site running with EECS servers at KU. Running Django through CGI with an .htaccess is a bit hackey, but it works. The currently functioning files are located in install/ folder, however in production they need to be placed slightly differently. .htaccess is designed to go directly in the root of public_html or similar while django.cgi should go in the cgi-bin.




=================
Appendix
=================
Miscilaneous information on getting setup on EECS servers

Easy Install for Virtualenv on EECS Machines
============================================

Install of any Python system is recommended in a virtual enviroment. Below is a rough idea of how to set this up on EECS servers.

# Install oh-my-zsh defualt install
wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
# Add a plugin to your ~/.zshrc file. Find the line that starts with plugins=(... and add the virtualenvwrapper plugin
plugins=(git virtualenvwrapper)
# Now go into zsh
zsh
# Download pip from source and untar and cd
wget https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz#md5=cbb27a191cebc58997c4da8513863153 && tar -xf pip-1.3.1.tar.gz && cd pip-1.3.1
# Install locally
python setup.py install --user
# Add to the end of your PATH in ~/.zshrc
/home/{{USERNAME}}/.local/bin
# reload PATH
source ~/.zshrc
# Install virtualenvwrapper finally
pip install virtualenvwrapper --user
# You might need to reload virtualenvwrapper now
source ~/.zshrc
# bask in the glow of a fresh virtualenv
mkvirtualenv testing
