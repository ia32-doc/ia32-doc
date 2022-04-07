import argparse

from ia32doc.doc import Doc
from ia32doc.processors.c_processor import DocCProcessor
from ia32doc.options import DocProcessorOptions


TEST = False
TEST_CONFIG = 'conf/default.yml'
TEST_FILE = 'yaml/Intel/VMX/index.yml'


def process(config, file):
    processor = DocCProcessor()
    options = DocProcessorOptions(file=config)
    with processor.opt.push(options):
        processor.run(Doc.parse(file))


def process_all():
    index = 'yaml/Intel/index.yml'
    process('conf/default.yml', index)
    process('conf/default_cpp.yml', index)
    process('conf/compact.yml', index)
    process('conf/defines_only.yml', index)


def test():
    process(TEST_CONFIG, TEST_FILE)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--config',
                        type=str, required=False,
                        default='conf/default.yml',
                        help='Configuration file')

    parser.add_argument('-f', '--file',
                        type=str, required=False,
                        help='YAML file to process. If not specified, all known files are processed')

    args = parser.parse_args()
    if args.file:
        process(args.config, args.file)
    else:
        process_all()


if __name__ == '__main__':
    if TEST:
        test()
    else:
        main()
