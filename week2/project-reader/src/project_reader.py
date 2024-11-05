from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_content = toml.loads(content)
        print(toml_content)
        name = toml_content['tool']['poetry'].get('name')
        description = toml_content['tool']['poetry'].get('description')
        license = toml_content['tool']['poetry'].get('license')
        authors = toml_content ['tool']['poetry'].get('authors')
        dependencies = toml_content['tool']['poetry'].get('dependencies')
        development_dependencies= toml_content['tool']['poetry']['group']['dev'].get('dependencies')

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, development_dependencies)


