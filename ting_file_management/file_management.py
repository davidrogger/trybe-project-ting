import sys


def txt_importer(path_file: str):
    valid_extension = "txt"
    if not path_file.endswith(valid_extension):
        return sys.stderr.write("Formato inválido\n")
    else:
        try:
            with open(path_file, "r") as file:
                file_content = file.read()
                lines = file_content.split("\n")
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        else:
            return lines
