from ting_file_management.priority_queue import PriorityQueue
import pytest

PRIORITY = dict()
PRIORITY["qtd_linhas"] = 4
PRIORITY["nome_do_arquivo"] = "file_priority.txt"
PRIORITY["linhas_do_arquivo"] = [
    'isto', 'é', 'um', 'arquivo', 'prioritário']

FILE_NOT_PRIORITY = dict()
FILE_NOT_PRIORITY["qtd_linhas"] = 8
FILE_NOT_PRIORITY["nome_do_arquivo"] = "file_not_priority.txt"
FILE_NOT_PRIORITY["linhas_do_arquivo"] = [
    'isto', 'não', 'é', 'um', 'arquivo', 'prioritário']


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    instance = PriorityQueue()
    assert instance.is_priority(FILE_NOT_PRIORITY) is False
    assert instance.is_priority(PRIORITY) is True

    instance.enqueue(PRIORITY)
    instance.enqueue(FILE_NOT_PRIORITY)
    assert len(instance.regular_priority) == 1
    assert len(instance.high_priority) == 1
    assert instance.search(0) == PRIORITY
    assert instance.search(1) == FILE_NOT_PRIORITY

    instance.dequeue()
    assert instance.search(0) == FILE_NOT_PRIORITY

    instance.dequeue()
    assert len(instance.high_priority) == 0
    with pytest.raises(IndexError):
        instance.search(2)
