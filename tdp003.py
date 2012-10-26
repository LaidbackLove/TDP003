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
    """renders the homepage"""
    return render_template('home_page.html' )

@app.route('/project')
def project_page():
    """"renders the project page with all data in the json file"""
    return render_template('project_page.html' ,data=projects)

@app.route('/technique')
def technique_page():
    """renders the technique page with the techniques as data"""
    return render_template('technique_page.html',data=tech)

@app.route("/project/<project_no>")
def show_project(project_no):
    """renders the project page with project id as data"""
    try:
        get_project=datalager.get_project(projects, int(project_no))
    except:
        return render_template("error_page.html", data=404)
    if int(project_no)>len(projects) or int(project_no)<=0:
        return render_template("error_page.html", data=404)
    return render_template("show_project.html",data=get_project)

@app.route("/search")
def show_search():
    return render_template("search_page.html", data=[])



@app.route("/search", methods=['POST'])
def search():
    """renders the search page with the variables from the searchbox"""
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
    """renders the technique page with a specific technique"""
    try:
        techniques=(tech[technique],technique)
    except:
        return render_template("error_page.html", data=404)
    return render_template("show_technique.html",data=techniques)

@app.errorhandler(404)
def error_page(error):
    """renders the error 404 page in the template"""
    return render_template("error_page.html", data=404)

if __name__ == '__main__':
    app.run()
