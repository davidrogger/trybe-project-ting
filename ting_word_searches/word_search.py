from ting_file_management.queue import Queue


def find_word_in_line(uncapitalize_word: str, lines: list, include_phrase):
    words_found = []
    for line, phrase in enumerate(lines, start=1):
        uncapitalize_phrase = phrase.lower()
        if uncapitalize_word in uncapitalize_phrase:
            data_found = {"linha": line}
            if include_phrase:
                data_found["conteudo"] = phrase
            words_found.append(data_found)
    return words_found


def generate_report_by_word(word: str, instance: Queue, include_phrase: bool):
    report = []
    uncapitalize_word = word.lower()

    for index in range(len(instance)):
        file_data = instance.search(index)
        path_file = file_data["nome_do_arquivo"]
        file_lines = file_data["linhas_do_arquivo"]
        words_found = find_word_in_line(
            uncapitalize_word, file_lines, include_phrase
        )

        if len(words_found):
            data_found = {
                "palavra": word,
                "arquivo": path_file,
                "ocorrencias": words_found,
            }
            report.append(data_found)

    return report


def exists_word(word: str, instance: Queue):
    return generate_report_by_word(word, instance, include_phrase=False)


def search_by_word(word: str, instance: Queue):
    return generate_report_by_word(word, instance, include_phrase=True)
