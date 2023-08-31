import sys 
import re
import requests

def dataset_exists(url):

    Files = ["application/zip" , "application/x-tar", "application/octet-stream", "application/x-tar-gz"]

    try:
        response = requests.head(url)
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '').lower()
            if content_type in Files:
                return True
            else:
                return False
        else:
            return False
    except requests.RequestException as e:
        print("Error:", e)
        return False

if __name__ == "__main__":
    # Regular expression to check if the url is valid for tar or zip files
    URL_REGEX = r'\bhttps?:\/\/\S+\.(?:tar|zip)\b'

    url = '{{ cookiecutter.url }}'
    task_category = '{{ cookiecutter.task_category }}'
    task = '{{cookiecutter.task}}'

    #fail if url is not tar or zip
    if not re.match(URL_REGEX, url):
        print("WARNING: Invalid url! file must be tar or zip")

    if not dataset_exists(url):
        print("WARNING: Invalid url! dataset does not exist.")

    #fail if task_category not in task and ignore if its other
    if task_category not in task and task != "other":
        sys.exit("ERROR: Invalid Combination! {{cookiecutter.task}} does not fall in the category {{cookiecutter.task_category}}.")
