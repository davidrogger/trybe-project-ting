from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def is_new_file(file_name: str, instance: Queue):
    instance_length = len(instance)
    for index in range(instance_length):
        element = instance.search(index)
        if element["nome_do_arquivo"] == file_name:
            return False

    return True


def process(path_file: str, instance: Queue):
    if is_new_file(path_file, instance):
        file_lines = txt_importer(path_file)

        file_report = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_lines),
            "linhas_do_arquivo": file_lines,
        }

        instance.enqueue(file_report)

        return sys.stdout.write(str(file_report))


def remove(instance: Queue):
    if len(instance):
        first_out = instance.dequeue()
        file_path = first_out["nome_do_arquivo"]
        return sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")
    else:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
