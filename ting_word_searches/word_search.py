def exists_word(word, instance):
    list = []
    search = []

    for index, line in enumerate(instance.queue[0]["linhas_do_arquivo"]):
        if word.casefold() in line.casefold():
            list.append({"linha": index + 1})

    for index in range(len(instance.queue)):
        if len(list) > 0:
            search.append({
                "palavra": word,
                "arquivo": instance.queue[index]["nome_do_arquivo"],
                "ocorrencias": list
            })

    return search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
