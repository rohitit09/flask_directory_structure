import os
# virtual_env1_create="python3 -m venv "


def setup_project():
    # os.system("pip3 install virtualenv")
    '''# requirnments_install="pip3 install -r <path to requirnmnets.txt file>"

    # for mac and python3 project

    # os.system(homebrew_install)
    # os.system(git_install)
    # os.system(get_pip_download)

    # set path to autoenv
    # os.system("brew install autoenv")
    # os.system("echo 'source $(brew --prefix autoenv)/activate.sh' >> ~/.bash_profile")'''
    # import ipdb; ipdb.set_trace()
    project_name=input("enter project name:")
    os.system("mkdir "+project_name+" && cd "+project_name+ " && mkdir "+project_name)
    os.chdir(os.getcwd()+"/"+project_name)
    os.system("python3 -m venv env_"+project_name)

    env_path="source env_"+project_name+"/bin/activate"
    # with open(".env","a") as fp:
    #     fp.write(env_path)
    
    os.chdir(os.getcwd()+"/"+project_name)
    os.system("echo 'flask' >> requirnments.txt")
    os.system("echo 'pymongo' >> requirnments.txt")
    #os.system("echo 'psycopg2' >> requirnments.txt")
    os.system("echo 'flask_sqlalchemy' >> requirnments.txt")

    print (os.getcwd())
    with open("README.md","w") as f:
        f.write("welocome  to "+project_name+" project")

    with open("config.py","w") as f:
        f.write("import os\n")
        f.write("#from pymongo import MongoClient\n")
        f.write("#from flask_sqlalchemy import SQLAlchemy\n\n")
        f.write("basedir = os.path.abspath(os.path.dirname(__file__))\n")
        f.write("SECRET_KEY = '12345thisismyscretkey47464674'\n\n")
        f.write("#client = MongoClient('localhost', 27017)\n")
        f.write("#db = SQLAlchemy()\n")
        f.write('#SQLALCHEMY_DATABASE_URI = "postgresql://localhost/rohit"')
        # class Config(object):
        # DEBUG = False
        # TESTING = False
        # CSRF_ENABLED = True
        # SECRET_KEY = 'this-really-needs-to-be-changed'
        # # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        # SQLALCHEMY_DATABASE_URI = "postgresql://localhost/rohit"
        # class ProductionConfig(Config):
        #     DEBUG = False
        # class StagingConfig(Config):
        #     DEVELOPMENT = True
        #     DEBUG = True
        # class DevelopmentConfig(Config):
        #     DEVELOPMENT = True
        #     DEBUG = True
        # class TestingConfig(Config):
        #     TESTING = True

    with open("run.py","w") as f:
        f.write("from apps import app\n")
        f.write("app.run(host='0.0.0.0',port=5000, debug=True,threaded=True)")

    # # #create an app
    app_name=input("enter app name:")

    os.system("mkdir apps && cd apps && mkdir "+app_name)
    print (os.getcwd())
    os.chdir(os.getcwd()+"/apps")

    with open("__init__.py","w") as f:
        # f.write("from apps import app\n")
        f.write("from flask import Flask\n")
        f.write("from ."+app_name+" import "+app_name+"\n")
        f.write("#add app\n")
        f.write("from  config import SECRET_KEY\n")
        f.write("#from  config import client\n")
        f.write("#from config import db,SQLALCHEMY_DATABASE_URI\n\n\n")
        f.write("def create_app():\n\t")
        f.write("app = Flask(__name__)\n\t")
        f.write("app.secret_key=SECRET_KEY\n\t")
        f.write("app.register_blueprint("+app_name+")\n\t")
        f.write("#add blueprint\n\t")
        f.write("#app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI\n\t")
        f.write("#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\n\t")
        f.write("#db.init_app(app)\n\t")
        f.write("return app\n\n\n")
        f.write("#def setup_database(app):\n\t")
        f.write("#with app.app_context():\n\t\t")
        f.write("#db.create_all()\n\n\n")
        f.write("app=create_app()\n")
        f.write("#setup_database(app)\n")
        
    os.chdir(os.getcwd()+"/"+app_name)

    os.system("mkdir static")
    os.system("mkdir templates")
    os.system("mkdir templates/"+app_name)

    with open("__init__.py","w") as f:
        # f.write("from apps import app\n")
        f.write("from flask import Blueprint\n")
        f.write(app_name+"=Blueprint('"+app_name+"', __name__,template_folder='templates',static_folder='static',static_url_path='/"+app_name+"/static')\n")
        f.write("from . import urls\n")

    with open("views.py","w") as f:
        # f.write("from apps import app\n")
        # f.write("from . import "+app_name+"\n")
        f.write("from . models import *\n")
        f.write("from flask import request,jsonify,render_template\n\n\n")
        f.write("def helloexample():\n\t")
        f.write("return jsonify({'msg':'Hi there its me!!'})\n\n")

        f.write("def firstapp():\n\t")
        f.write("return jsonify({'msg':'"+app_name+" app'})\n\n")

        f.write("def firsthtml():\n\t")
        f.write("return render_template('"+app_name+"/index.html')\n")

    with open("urls.py","w") as f:
        # f.write("from apps import app\n")
        f.write("from . import "+app_name+"\n")
        f.write("from . models import *\n")
        f.write("from . views import firstapp, firsthtml, helloexample\n")
        f.write("from flask import request,jsonify\n\n\n")
        f.write(app_name+".add_url_rule('/',methods=['GET'], view_func=helloexample)\n")
        f.write(app_name+".add_url_rule('/"+app_name+"/firstapp',methods=['GET'], view_func=firstapp)\n")
        f.write(app_name+".add_url_rule('/"+app_name+"/firsthtml',methods=['GET'], view_func=firsthtml)\n")

    with open("models.py","w") as f:
        # f.write("from apps import app\n")
        f.write("#from config import client\n")
        f.write("#from config import db\n")

    with open("templates/"+app_name+"/index.html","w") as f:
        # f.write("from apps import app\n")
        f.write("<p>hello "+app_name+"</p>\n")

    print("\n$$$$$$$$$$$$$$  Project Created $$$$$$$$$$$$$$$$n")
    print("1. First go to the directory $cd "+project_name)
    print("2. Activate environment env_"+project_name)
    print("\t$"+env_path)
    print("3. Go to the project directory $cd "+project_name)
    print("4. Install dependency from requirnments.txt")
    print("\t$pip3 install -r requirnments.txt")
    print("5. Run application using:\n\t$python3 run.py")
    print("6. To test this application type below link in Browser:")
    print("\tlocalhost:5000/")
    print("\tlocalhost:5000/"+app_name+"/firstapp")
    print("\tlocalhost:5000/"+app_name+"/firsthtml\n\n")


def create_new_app():
    app_name=input("enter app name:")
    os.chdir(os.getcwd()+"/apps")
    with open("__init__.py","r") as f:
        data=f.read()
        data1=data.split("#add app")
        data0=data1[0]
        # import ipdb; ipdb.set_trace()
        data0=data0+"from ."+app_name+" import "+ app_name+"\n"+"#add app"
        data1=data0+data1[1]
        data1=data1.split("#add blueprint")
        data0=data1[0]
        data0=data0+"app.register_blueprint("+app_name+")"+"\n\t#add blueprint"
        data1=data0+data1[1]
        
    with open("__init__.py","w") as f:
        f.write(data1)

    os.system("mkdir "+app_name)    
    os.chdir(os.getcwd()+"/"+app_name)

    os.system("mkdir static")
    os.system("mkdir templates")
    os.system("mkdir templates/"+app_name)

    with open("__init__.py","w") as f:
        # f.write("from apps import app\n")
        f.write("from flask import Blueprint\n")
        f.write(app_name+"=Blueprint('"+app_name+"', __name__,template_folder='templates',static_folder='static',static_url_path='/"+app_name+"/static')\n")
        f.write("from . import urls\n")

    with open("views.py","w") as f:
        # f.write("from apps import app\n")
        # f.write("from . import "+app_name+"\n")
        f.write("from . models import *\n")
        f.write("from flask import request,jsonify,render_template\n\n\n")
        f.write("def helloexample():\n\t")
        f.write("return jsonify({'msg':'Hi there its me!!'})\n\n")

        f.write("def firstapp():\n\t")
        f.write("return jsonify({'msg':'"+app_name+" app'})\n\n")

        f.write("def firsthtml():\n\t")
        f.write("return render_template('"+app_name+"/index.html')\n")

    with open("urls.py","w") as f:
        # f.write("from apps import app\n")
        f.write("from . import "+app_name+"\n")
        f.write("from . models import *\n")
        f.write("from . views import firstapp, firsthtml, helloexample\n")
        f.write("from flask import request,jsonify\n\n\n")
        f.write(app_name+".add_url_rule('/',methods=['GET'], view_func=helloexample)\n")
        f.write(app_name+".add_url_rule('/"+app_name+"/firstapp',methods=['GET'], view_func=firstapp)\n")
        f.write(app_name+".add_url_rule('/"+app_name+"/firsthtml',methods=['GET'], view_func=firsthtml)\n")

    with open("models.py","w") as f:
        # f.write("from apps import app\n")
        f.write("#from config import client\n")
        f.write("#from config import db\n")

    with open("templates/"+app_name+"/index.html","w") as f:
        # f.write("from apps import app\n")
        f.write("<p>hello "+app_name+"</p>\n")

    print("\nNew app added successfully to project :)")
    print("To test this new app run the project and paste below link to Browser:")
    print("\tlocalhost:5000/"+app_name+"/firstapp")
    print("\tlocalhost:5000/"+app_name+"/firsthtml")

if __name__=='__main__':
    inpt=input("Creating new project type YES/NO:").lower()
    if inpt=="yes" or inpt=="y":
        setup_project()
    elif inpt=="no" or inpt=="n":
        inpt= input("Want to add new app to existing project type YES/NO:").lower()
        if inpt=="yes" or inpt=="y":
            try:
                create_new_app()
            except FileNotFoundError as e:
                print(str(e))
                print("\n### Check are you in project Directoy? ###")
                print("If no please go to project directory and try again!!\n")
        elif inpt=="no" or inpt=="n":
            exit(0)
        else:
            print("Incorrect input please try again!!")
    else:
        print("Incorrect input please try again!!")


