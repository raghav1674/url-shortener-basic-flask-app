from flask import Blueprint, render_template, redirect, url_for, request
from .utils.file_handler import check_code, get_url


# create a blueprint object
bp = Blueprint('main', __name__, template_folder='templates')

# index route


@bp.route("/", methods=['GET'])
def index():
    return render_template('index.html')

# create the short url


@bp.route("/create_url", methods=['GET', 'POST'])
def create_url():
    if request.method == 'POST':
        code = request.form['code']
        url = request.form['url']
        created, new_url = check_code(code, url, "urls.json")
        if created:
            return new_url
        return "Code already present"
    return "Method not Supported"

# get the real url corresponding to the code given


@bp.route("/<string:code>", methods=['GET'])
def get_link(code):
    found, real_url = get_url(code, "urls.json")
    if found:
        return redirect(real_url)
    return real_url


# @bp.route("/logout")
# def logout():
#     return redirect(url_for('main.index'))  # here index is a function name
# # redirect changes the url also  and main is the view name which we have set in Blueprint object.
# also set FLASK_APP=filename and set FLASK_ENV=development and do flask run