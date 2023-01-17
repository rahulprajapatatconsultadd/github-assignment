from django.shortcuts import render, HttpResponseRedirect
from .validator.validator import Validator
from urllib.parse import urlparse
from pathlib import Path
from os.path import join
import logging

# Create your views here.
def dump_url_to_file(url: str):
    try:
        path = join(Path(__file__).resolve().parent.parent, 'github_project', 'url',  'urls.txt')
        if not ('http' in url or 'https' in url):
            url = 'http://' + url
        organization = urlparse(url).path[1:]
        
        with open(path, 'w') as file:
            file.writelines([url, '\n', organization])
    except Exception as e:
        logging.error(e)


def home_page(request):
    try:  
        if request.method == 'POST':
            validate = Validator()
            # logging.info('############Validator Working')
            print('####Validate Check')
            url = request.POST.get('urls')   
            print('*********url_validator.home_page.URL',url)
            # logging.info('##########Url : ', url)        
            try:
                if validate.url_validator(url):
                    print("###INSIDE url_validator if")
                    dump_url_to_file(url)
                    return HttpResponseRedirect('../commits/')
                return render(request, 'url_validator/not_valid.html',{})
            except Exception as e:
                # logging.error("Error Msg : ",str(e)) 
                print("$$$$$$$Error Msg 36: ",e)                   
        return render(request, 'url_validator/index.html',{})
    
    except Exception as e:
        print("^^^^^^^Error Msg 40 : ", e)
        # logging.error(e)