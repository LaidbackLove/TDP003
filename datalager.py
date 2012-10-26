# -*- coding: utf-8 -*-
import json
import operator
import datetime

def load(filename):
    """loads a file with json data and returns the data"""
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file, "UTF-8") #format data to utf8 if we get a error we return None
    except:
        print_log(('  load('+filename+')  '), 'error2 json file does not exist  ')
        return []
    print_log(('  load('+filename+')  '), '0 OK  ')
    return data

def get_project_count(db):

    """returns the number of projects in db"""
    print_log('  get_project_count(db)  ', '0 OK  ')
    return len(db)
    
def get_project(db, id):
    """returns the project with the specific id"""
    for dictionary in db:
        if dictionary['project_no']==id: #checks id against project_no in db
            print_log('  get_project(db, id)  ', '0 OK  ')
            return dictionary

def sort_db(db, sort_by='project_name', sort_order='ascending'):

    db.sort(key=operator.itemgetter(sort_by))
    if sort_order=='desc':
        db.reverse()
    print_log('  db_sort(db,sort_by,sort_order)  ', '0 OK  ')
    return db

def get_active_projects(db):
    active_projects=[]
    db.sort(key=operator.itemgetter('start_date'))
    for n in range(0,3):
        active_projects.append(db[n])
    print_log('  get_active_projects(db)  ', '0 OK  ')
    return active_projects.reverse()


def get_techniques(db):
    """returns all techniques used in projects in a sorted list"""
    techniques=[]
    for dictionary in db:
        techniquelist=dictionary['techniques_used'] #checks if the list of techniques is in the project
        for x in techniquelist:
            if techniques.count(x)==0: #append to techniques if its not in the list
                techniques.append(x)
    print_log('  get_techniques(db)  ', '0 OK  ')
    return sorted(techniques)

def get_technique_stats(db):
    """returns a dictionary containing the techniques as keys and the projects where they are used as values"""
    db.reverse()
    temp_dict={'id' : 0, 'name' : ' '}
    templist=[]
    technique_dict=dict.fromkeys(get_techniques(db),[])
    for key in technique_dict:
        for dictionary in db:
            if key in dictionary['techniques_used']:#checks if the key is in the dictionary
                temp_dict['id']=dictionary['project_no']
                temp_dict['name']=dictionary['project_name'] #puts the right values in the dictionary
                templist.append(temp_dict) #appends the dictionary to templist
                technique_dict[key]=templist
                temp_dict={} #resets the dictionary
        templist=[]
    return (technique_dict)

def search(db,sort_by=u'start_date',sort_order=u'asc',techniques=None,search=None, search_fields=None):
    """searches for a project and returns a list of dictionaries that fit the search criteria"""
    techniquelist=[]
    result_of_search=[]
    if techniques==[]: 
        techniques=None
    if search!=None:
        try:
            search=unicode(search,'utf-8')
        except TypeError:
            pass
        search=search.lower()
    #if techniques are given we put them in a list
    if techniques!=None:
        for dictionary in db:
            for technique in dictionary['techniques_used']: #for every technique in all the projects if it's in techniques
                if technique in techniques:
                    techniquelist.append(dictionary) 
                    break

    #if search_field is given only those fields are searched
    if search_fields!=None:
        try:
            search=search.encode('utf-8')
        except TypeError:
            pass
        try:
            search_fields=search_fields.encode('utf-8')
        except TypeError:
            pass


            for dictionary in db:
             for value in search_fields:
                 if search in str(dictionary[value]):
                     result_of_search.append(dictionary) #if value matches search add to result_of_search
                     break

    #searches for a string
    if search!=None:
        for dictionary in db:
            for key in dictionary:
                key_in_dict=dictionary[key] #unicode(dictionary[key],'utf-8')
                if isinstance(key_in_dict, int): #we want to check if key_in_dict is a string and if isinstance(key_in_dict, str) always returned true so we did it the other way around
                    pass
                elif isinstance(key_in_dict, list):
                    pass
                else:
                    key_in_dict=key_in_dict.lower()
                if search in str(key_in_dict) and key_in_dict in techniquelist:
                    result_of_search.append(dictionary) #if true append to result of search and break the loop
                    break
                elif str(key_in_dict) in search_fields:
                    result_of_search.append(dictionary) #if true append to result of search and break the loop
                    break
                elif search in str(key_in_dict) and techniques==None:
                    result_of_search.append(dictionary) #if true append to result and break loop
                    break


    #sorts the result 
    if result_of_search==[] and techniquelist==[]:
        db.sort(key=operator.itemgetter(sort_by)) #sorts db by sort_by
    else:
        techniquelist.sort(key=operator.itemgetter(sort_by))
        result_of_search.sort(key=operator.itemgetter(sort_by)) #sort by the field sort_by
    if sort_order=='desc':
        techniquelist.reverse()
        result_of_search.reverse() #reverses the list if the sort order is descending
        db.reverse()
    if search_fields==[]:
        print_log('  search('+search+')'  , '0 OK  ')
        return [] #if we search for no fields return empty list
    #returns the correct list
    if techniquelist==[] and result_of_search==[] and search=="":
        print_log('  search('+search+')'  , '0 OK  ')
        return db #if we get no result return original list
    elif techniquelist==[] and result_of_search==[] and search!=None:
        print_log('  search('+search+')'  , '0 OK  ')
        return []
    elif result_of_search==[]:
        print_log('  search('+search+')'  , '0 OK  ')
        return techniquelist #if we search for techniques return projects with the techniques
    else:
        print_log('  search('+search+')'  , '0 OK  ')
        return result_of_search #returns projects that are searched for

def print_log(message, error):
    log=open('log.txt', 'a')
    timestamp=datetime.datetime.now()
    log.write(str(timestamp))
    log.write("    ")
    log.write(error)
    log.write(message)
    log.write('\n')