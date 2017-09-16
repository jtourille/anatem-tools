import os
import re
import requests


PARAMS = {
    "annotators": "tokenize,ssplit,pos,lemma,ner",
    "outputFormat": "json",
    "tokenize.whitespace": "true",
    "ssplit.eolonly": "true"
}


def add_corenlp_features(corpus_file, output_file, corenlp_url):
    """
    Add CoreNLP features to corpus part file
    :param corpus_file: corpus file
    :param output_file: output file path
    :param corenlp_url: CoreNLP server URL
    :return: nothing
    """

    all_sequences = list()

    with open(os.path.abspath(corpus_file), "r", encoding="UTF-8") as input_file:
        current_tokens = list()

        for line in input_file:

            # Match an empty line = end of sequence marker
            if re.match("^$", line):
                if len(current_tokens) > 0:
                    processed_sequence = process_sequence(current_tokens, corenlp_url)
                    all_sequences.append(processed_sequence)
                    current_tokens.clear()
                continue

            token = {
                "form": line.rstrip("\n").split("\t")[0],
                "label": line.rstrip("\n").split("\t")[1]
            }
            current_tokens.append(token)

        if len(current_tokens) > 0:
            processed_sequence = process_sequence(current_tokens, corenlp_url)
            all_sequences.append(processed_sequence)

    write_to_file(all_sequences, output_file)


def write_to_file(sequences, output_file):
    """
    Write sequences to output file
    :param sequences: sequences to write
    :param output_file: output file path
    :return: nothing
    """

    with open(os.path.abspath(output_file), "w", encoding="UTF-8") as output_file:
        for sequence in sequences:
            for tok in sequence:
                output_file.write("{}\t{}\t{}\t{}\t{}\n".format(
                    tok["form"],
                    tok["lemma"],
                    tok["pos"],
                    tok["ner"],
                    tok["label"]
                ))

            output_file.write("\n")


def process_sequence(tokens, corenlp_url):
    """
    Process one sequence with CoreNLP
    :param tokens: tokens to process
    :param corenlp_url: CoreNLP server URL
    :return: processed sequence
    """

    # Building sentence string
    sent_str = " ".join(tok["form"] for tok in tokens)

    # Processing sentence
    r = requests.post(corenlp_url, params=PARAMS, data=sent_str.encode("UTF-8"))

    # Getting json answer
    r_json = r.json()

    # Fetching first and only sentence in the answer (options in PARAMS disallow multiple sentences)
    core_tokens = r_json["sentences"][0]["tokens"]

    # Will contain the sequence with CoreNLP features
    payload = list()

    for tok_ori, tok_cor in zip(tokens, core_tokens):
        for k, v in tok_cor.items():
            tok_ori[k] = v
        payload.append(tok_ori)

    return payload
