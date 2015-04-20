# py-tdd
## Going through the Test-Driven Development with Python

Just reading [this excellent book](http://obeythetestinggoat.com/).

### Setup on Debian 7.x

1. Install `python` and `pip`(as root or sudoer):

    `apt-get install python3 python3-pip`

2. Install virtualenv and virtualenvwrapper(as regular user):

    `pip3 install virtualenvwrapper`

3. Add these lines to your `.bashrc`:

    ```bash
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/prj
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh
    ```

4. Source your new configuration:

    `source ~/.bashrc`

5. Create new virtual environment:

    `mkvirtualenv py-tdd-env`

6. Install required dependencies:

    pip3 install django==1.7
    pip3 install --upgrade selenium


