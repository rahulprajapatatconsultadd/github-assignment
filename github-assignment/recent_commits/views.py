from pathlib import Path
from os.path import join
from mimetypes import guess_type
from .commits_folder.csv_operations import CsvOperation
from .commits_folder.github_organisation import GithubOrganisation
from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    try:
        csv_op = CsvOperation()
        print("Success csv_op")
        github = GithubOrganisation()
        print("###Before dump")
        github.dump_all_commits_in_csv()
        print("###After dump")
        csv_op.sort_csv()
        print("###After sort")
        csv_op.csv_to_json()
        return render(request, "recent_commits/index.html",{})
    except Exception as e:
        print("####Error Message at recent_comits.views.homepage",e)
        return HttpResponse("Some Error Occured",status=404)
        

    
def download_file(request):
    try:
        filepath = Path(__file__).resolve().parent.parent
        filepath = join(filepath, 'github_project/json/info.json')
        filename = 'info.json'
        
        file = open(filepath, 'r')
        mime_type, _ = guess_type(filepath)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename=' + filename     
        return response
    except Exception as e:
        print("####Error Message at recent_comits.views.download_file",e)