import argparse

from ia32doc.doc import Doc
from ia32doc.processors.c_processor import DocCProcessor
from ia32doc.options import DocProcessorOptions


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--config',
                        type=str, required=False,
                        default='conf/default.yml',
                        help='Configuration file')

    parser.add_argument('-f', '--file',
                        type=str, required=True,
                        help='YAML file to process')

    args = parser.parse_args()

    # doc_list = Doc.parse('yaml/Intel/index.yml')
    # doc_list = Doc.parse('yaml/Intel/CPUID/index.yml')
    # doc_list = Doc.parse('yaml/Intel/VMX/index.yml')
    doc_list = Doc.parse(args.file)

    processor = DocCProcessor()
    options = DocProcessorOptions(file=args.config)
    with processor.opt.push(options):
        processor.run(doc_list)


if __name__ == '__main__':
    main()
