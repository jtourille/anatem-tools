import argparse
import logging
import os
import time
from datetime import timedelta

from anatem.convert import regroup_documents, lower_and_replace, convert_to_one_class
from anatem.corenlp import add_corenlp_features

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title="Sub-commands", description="Valid sub-commands",
                                       help="Valid sub-commands", dest="subparser_name")

    # Regroup documents from a corpus part into one document
    parser_regroup = subparsers.add_parser('REGROUP', help="Regroup documents from one part into one document")
    parser_regroup.add_argument("--input_path", help="Path to the corpus part", dest="input_path", type=str,
                                required=True)
    parser_regroup.add_argument("--output_file", help="Output file path", dest="output_file", type=str, required=True)

    # Lowercase and replace digits in one document
    parser_preproc = subparsers.add_parser('PREPROC', help="Lowercase and replace digits into one document")
    parser_preproc.add_argument("--input_file", help="Input file path", dest="input_file", type=str,
                                required=True)
    parser_preproc.add_argument("--output_file", help="Output file path", dest="output_file", type=str, required=True)

    # Lowercase and replace digits in one document
    parser_convert = subparsers.add_parser('CONVERT', help="Convert multi-class IOB scheme to one-class IOB scheme")
    parser_convert.add_argument("--input_file", help="Input file path", dest="input_file", type=str,
                                required=True)
    parser_convert.add_argument("--output_file", help="Output file path", dest="output_file", type=str, required=True)

    # Add corenlp features to corpus
    parser_corenlp = subparsers.add_parser('CORENLP', help="Add features extracted from CoreNLP")
    parser_corenlp.add_argument("--input_file", help="Input file path", dest="input_file", type=str,
                                required=True)
    parser_corenlp.add_argument("--output_file", help="Output file path", dest="output_file", type=str, required=True)
    parser_corenlp.add_argument("--corenlp_url", help="CoreNLP server URL", dest="corenlp_url", type=str, required=True)

    args = parser.parse_args()

    if args.subparser_name == "REGROUP":

        # Logging to stdout
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

        # Checking if output file exists
        if os.path.isfile(os.path.abspath(args.output_file)):
            raise FileExistsError("The output file already exists: {}".format(
                os.path.abspath(args.output_file)
            ))

        # Checking id input directory exists
        if not os.path.isdir(os.path.abspath(args.input_path)):
            raise NotADirectoryError("The input path you specified doest not exist or is not a directory: {}".format(
                os.path.abspath(args.input_path)
            ))

        logging.info("Starting regrouping documents in one document")
        logging.info("* source directory: {}".format(os.path.abspath(args.input_path)))
        logging.info("* target file: {}".format(os.path.abspath(args.output_file)))

        start = time.time()

        # Regrouping documents
        regroup_documents(args.input_path, args.output_file)

        end = time.time()

        logging.info("Done ! (Time elapsed: {})".format(timedelta(seconds=round(end-start))))

    elif args.subparser_name == "PREPROC":

        # Checking if output file exists
        if os.path.isfile(os.path.abspath(args.output_file)):
            raise FileExistsError("The output file already exists: {}".format(
                os.path.abspath(args.output_file)
            ))

        # Checking if input file exists
        if not os.path.isfile(os.path.abspath(args.input_file)):
            raise FileNotFoundError("The input file you specified does not exist: {}".format(
                os.path.abspath(args.input_file)
            ))

        start = time.time()

        # Lowercasing and replacing digits
        lower_and_replace(args.input_file, args.output_file)

        end = time.time()

        logging.info("Done ! (Time elapsed: {})".format(timedelta(seconds=round(end-start))))

    elif args.subparser_name == "CONVERT":

        # Checking if output file exists
        if os.path.isfile(os.path.abspath(args.output_file)):
            raise FileExistsError("The output file already exists: {}".format(
                os.path.abspath(args.output_file)
            ))

        # Checking if input file exists
        if not os.path.isfile(os.path.abspath(args.input_file)):
            raise FileNotFoundError("The input file you specified does not exist: {}".format(
                os.path.abspath(args.input_file)
            ))

        start = time.time()

        # Starting conversion
        convert_to_one_class(args.input_file, args.output_file)

        end = time.time()

        logging.info("Done ! (Time elapsed: {})".format(timedelta(seconds=round(end-start))))

    elif args.subparser_name == "CORENLP":

        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

        # Checking if output file exists
        if os.path.isfile(os.path.abspath(args.output_file)):
            raise FileExistsError("The output file already exists: {}".format(
                os.path.abspath(args.output_file)
            ))

        # Checking if input file exists
        if not os.path.isfile(os.path.abspath(args.input_file)):
            raise FileNotFoundError("The input file you specified does not exist: {}".format(
                os.path.abspath(args.input_file)
            ))

        start = time.time()

        add_corenlp_features(args.input_file, args.output_file, args.corenlp_url)

        end = time.time()

        logging.info("Done ! (Time elapsed: {})".format(timedelta(seconds=round(end - start))))