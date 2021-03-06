from flask import Blueprint,render_template,request,jsonify


route_user = Blueprint('user_page', __name__)

@route_user.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('user/login.html')

    resp = {'code':200, 'msg':'登录成功', 'data':{}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name)<1:
        resp['code']=-1
        resp['msg']= u"请输入正确的用户名！"
        return jsonify(resp)

    if login_pwd is None or len(login_pwd)<1:
        resp['code']=-1
        resp['msg']= u"请输入正确的密码！"
        return jsonify(resp)

    return '%s-%s'%(login_name,login_pwd)

@route_user.route('/edit')
def edit():
    return render_template('user/edit.html')

@route_user.route('/reset_pwd')
def reset_pwd():
    return render_template('user/reset_pwd.html')