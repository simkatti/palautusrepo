class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n".join(f"- {d}" for d in dependencies) if dependencies else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:"
            f"\n{self._stringify_dependencies(self.authors)}"
            f"\n"
            f"\nDependencies:"
            f"\n{self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:"
            f"\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
