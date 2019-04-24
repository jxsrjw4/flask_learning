from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import  Manager

import os

class Application( Flask ):
    def __init__(self, import_name, template_folder=None, root_path=None, static_folder=None):

        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,static_folder=static_folder)

        self.config.from_pyfile('config/base_setting.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])

        if self.config['ENVIROMENT']:
            self.config.from_pyfile('config/%s_setting.py' % self.config['ENVIROMENT'])

        db.init_app(self)



db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd()+'/web/templates',root_path=os.getcwd())
manager = Manager(app)

from common.models.suppliers import  Supplier
with app.app_context():
    db.create_all()  # 把所有的数据模型映射到数据库中


##
##静态方法插入
##
from common.libs.UrlManager import  UrlManager
app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")
app.add_template_global(UrlManager.buildUrl, "buildUrl")

