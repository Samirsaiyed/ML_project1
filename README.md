# ML_project1

## software and account requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS code IDE](https://code.visualstudio.com/doenload)
4. [GIT cli](https://git-scm.com/downloads)


Creating conda environment
'''
conda create -p venv python==3.7 -y
'''

'''
conda activate venv/
'''
OR
'''
conda activate venv
'''

'''
pip install -r requirements.txt
'''

To Add files to git
'''
git add .
'''

OR
'''
git add <file_name>
'''

notes > To ignore or folder from git we can write name of file or folder in .gitignore file

To check the git status
'''
git status
'''

To check all version maintained by git
'''
git log
'''

To create version/commit all changes by git 
'''
git commit -m "message"
'''

TO send version/changes to github
'''
git push origin main
'''

To check remote url
'''
git remote -v
'''

TO setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = samirsaiyed49@gmail.com
2. HEROKU_API_KEY = 
3. HEROKU_APP_NAME = 

BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> . 
> notes : image name for docker must be lowercase