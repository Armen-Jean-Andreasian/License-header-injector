import os


class LicenceInjector:
    def __init__(
        self,
        licence_header_text: str,
        file_extensions: tuple[str] = ('.py', '.go', '.c', '.cpp'),
        directory: str = '.'
    ):
        self.licence_header_text = licence_header_text
        self.file_extensions = file_extensions
        self.directory = directory

    def _inject_into_file(self, file_path: str):
        with open(file_path, mode='r+') as file:
            content = file.read()
            if not content.startswith(self.licence_header_text):
                upd_content = self.licence_header_text + '\n' + content
                file.seek(0)
                file.write(upd_content)

    def _recursive_injection(self):
        for root, _, files in os.walk(self.directory):
            for filename in files:
                if any(filename.endswith(ext) for ext in self.file_extensions):
                    file_path = os.path.join(root, filename)
                    self._inject_into_file(file_path)

    def inject(self):
        return self._recursive_injection()
