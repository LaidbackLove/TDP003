"-*-coding utf-8-*-"

from flask import Flask, request, url_for, render_template
import datalager

projects=datalager.load("data.json")
list_projects=projects
tech=datalager.get_technique_stats(projects)
search_projects=datalager.load("data.json")

app = Flask(__name__)
app.debug=True

@app.route('/')
def home_page():
    return render_template('home_page.html' )

@app.route('/project', methods=['POST', 'GET'])
def project_page():
    return render_template('project_page.html' ,data=projects)

@app.route('/list')
def list_page():
    return render_template('list_page.html')

@app.route('/technique')
def technique_page():
    return render_template('technique_page.html',data=tech)

@app.route("/project/<project_no>", methods=['POST', 'GET'])
def show_project(project_no):
    lol2=project_no

    lol=datalager.get_project(projects, int(lol2))



    return render_template("show_project.html",data=lol)

@app.route("/search", methods=['POST', 'GET'])
def search():
    term = request.form['key']
    sort_by = request.form['sort_by']
    search_by = request.form['search_by']
    sort_order = request.form['sort_order']
    if sort_order == 'Descending':
        sort_order = 'desc'
    else:
        sort_order = 'asc'
    search_result=datalager.search(db=search_projects, sort_order = sort_order, search=term, sort_by=sort_by, search_fields=search_by)
    return render_template("search_page.html",data=search_result)

@app.route("/technique/<technique>")
def show_technique(technique):
    lol3=(tech[technique],technique)

    return render_template("show_technique.html",data=lol3)

@app.errorhandler(404)
def error_page(error):
    return render_template("error_page.html", data=404)

if __name__ == '__main__':
    app.run()
