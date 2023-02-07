import sys


def txt_importer(path_file):
    if not path_file.endswith('txt'):
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, 'r') as file:
            content = file.read()
            list = content.split('\n')
            return list

    # Ref: Course e https://learnpython.com/blog/python-standard-error-stream/

    except OSError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
