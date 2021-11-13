from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        converted_content = tomli.loads(content)['tool']['poetry']
        print(converted_content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(converted_content['name'], converted_content['description'], converted_content['dependencies'], converted_content['dev-dependencies'])
