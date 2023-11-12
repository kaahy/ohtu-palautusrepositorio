from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        x = toml.loads(content)
        name = x['tool']['poetry']['name']
        description = x['tool']['poetry']['description']
        license = x['tool']['poetry']['license']
        authors = x['tool']['poetry']['authors']
        dependencies = dict.keys(x['tool']['poetry']['dependencies'])
        dev_dependencies = dict.keys(x['tool']['poetry']['group']['dev']['dependencies'])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
