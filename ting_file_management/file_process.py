from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    content = txt_importer(path_file)
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": (content),
    }
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(file)
    return sys.stdout.write(str(file))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write('Não há elementos\n')

    path_file = instance.dequeue()['nome_do_arquivo']
    return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return sys.stdout.write(str(file))

    except IndexError:
        return sys.stderr.write('Posição inválida\n')
