from flask.views import MethodView
from flask import render_template, redirect, request
from utils.search import Search
from utils.crawl import Crawl


class Home(MethodView):
    def get(self):
        return render_template("main/index.html")
    
    def post(self):
        form_data = request.form
        query = form_data.get('query')
        algorithm = form_data.get('algorithm')
        return redirect(f"/result?query={query}&algorithm={algorithm}")


class ResultPage(MethodView):
    def get(self):
        result = None
        query = request.args.get('query')
        algorithm = request.args.get('algorithm')
        if(query is None): return redirect('/')
        search = Search(query)
        print(type(search))
        if not search:
            print("Search is empty")
        else:
            print("Search is not empty")


        if algorithm == 'tfidf':
            result = search.search_using_cosinesimilarity()
        elif algorithm == 'and':
            result = search.search_using_and()
        elif algorithm == 'or':
            result = search.search_using_or()
        else:
            return redirect('/')
        return render_template("main/resultpage.html", query=query, algorithm=algorithm, result = result)

class CrawlResult(MethodView):
    def get(self):
        crw = Crawl()
        crw.make_crawl()
        return redirect("/")

