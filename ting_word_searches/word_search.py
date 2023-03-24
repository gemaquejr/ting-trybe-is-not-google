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
    list_of_words = []

    for item in instance.queue:
        object_to_append = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        number_line = 1
        for line in item["linhas_do_arquivo"]:
            if word.upper() in line.upper():
                object_to_append["ocorrencias"].append(
                    {"linha": number_line, "conteudo": line}
                )

            number_line += 1

        if len(object_to_append["ocorrencias"]) != 0:
            list_of_words.append(object_to_append)

        object_to_append["ocorrencias"] == []

    return list_of_words
