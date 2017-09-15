import os
import re


def regroup_documents(corpus_path, target_file):
    """
    Regroup corpus part into one document
    :param corpus_path: path to the corpus part
    :param target_file: target file path
    :return: nothing
    """

    all_sequences = list()

    for root, dirs, files in os.walk(os.path.abspath(corpus_path)):
        for filename in files:
            if re.match("^.*\.conll", filename):
                current_sequence = list()

                with open(os.path.join(root, filename), "r", encoding="UTF-8") as input_file:
                    for line in input_file:

                        if re.match("^$", line):
                            if len(current_sequence) > 0:
                                all_sequences.append("".join(current_sequence))
                                current_sequence.clear()

                            continue

                        current_sequence.append(line)

                    if len(current_sequence) > 0:
                        all_sequences.append("".join(current_sequence))

                with open(os.path.abspath(target_file), "w", encoding="UTF-8") as output_file:
                    output_file.write(
                        "{}".format("\n".join(all_sequences))
                    )


def lower_and_replace(source_file, target_file):
    """
    Lowercasing tokens and replacing digits by 0
    :param source_file: input file path
    :param target_file: output file path
    :return:
    """

    with open(os.path.abspath(source_file), "r", encoding="UTF-8") as input_file:
        with open(os.path.abspath(target_file), "w", encoding="UTF-8") as output_file:
            for line in input_file:
                if re.match("^$", line):
                    output_file.write("\n")
                    continue

                parts = line.rstrip("\n").split('\t')
                parts[0] = parts[0].lower()
                parts[0] = re.sub("\d", "0", parts[0])

                output_file.write("{}\n".format("\t".join(parts)))


def convert_to_one_class(source_file, target_file):
    """
    Convert multi-class IOB scheme into one-class IOB scheme
    :param source_file: input file path
    :param target_file: target file path
    :return:
    """

    with open(os.path.abspath(source_file), "r", encoding="UTF-8") as input_file:
        with open(os.path.abspath(target_file), "w", encoding="UTF-8") as output_file:
            for line in input_file:
                if re.match("^$", line):
                    output_file.write("\n")
                    continue

                parts = line.rstrip("\n").split('\t')
                if parts[1].startswith("B"):
                    parts[1] = "B"
                elif parts[1].startswith("I"):
                    parts[1] = "I"

                output_file.write("{}\n".format("\t".join(parts)))
