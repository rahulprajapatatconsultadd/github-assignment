import pandas
from pathlib import Path
from os.path import join
from mimetypes import guess_type
from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.
BASE_DIR = join(Path(__file__).resolve().parent.parent, 'github_project')
CSV_FILE = join(BASE_DIR, 'csv', 'all_commits.csv')
NEW_FILE = join(BASE_DIR, 'csv', 'contributors.csv')


def home_page(request):
    data = pandas.read_csv(CSV_FILE)
    dataframe = pandas.DataFrame(data)
    # Taking counts of commit and filtering out top 10 committers.
    top_contributors = dataframe['username'].value_counts().nlargest(20).reset_index()
    # Dumping the list of top contributors into csv file.
    top_contributors.columns = ['username', 'commit_count']
    top_contributors.to_csv(NEW_FILE, index=False)

    return render(request, 'top_committers/index.html')


def download_file(request):
    file = open(NEW_FILE, 'r')
    filename = 'contributors.csv'
    mime_type, _ = guess_type(NEW_FILE)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename

    return response
