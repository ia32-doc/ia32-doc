import argparse
import os

from ia32doc.doc import Doc
from ia32doc.processors.c_processor import DocCProcessor
from ia32doc.processors.python.python_processor import DocPythonProcessor
from ia32doc.options import DocProcessorOptions

ALL = False

TEST = False
PYTHON = False
TEST_CONFIG = 'conf/default.yml'
TEST_FILE = 'yaml/Intel/VMX/index.yml'


def process(processor_type, config, file):
    if 'c' == processor_type:
        processor = DocCProcessor()
    elif 'python' == processor_type:
        # TODO: Create valid python options
        output_directory = os.path.join("out", "python")
        processor = DocPythonProcessor(output_directory)
    else:
        raise ValueError(f"Unsupported processor {processor_type}")

    options = DocProcessorOptions(file=config)
    with processor.opt.push(options):
        processor.run(Doc.parse(file))


def process_all():
    index = 'yaml/Intel/index.yml'
    process('c', 'conf/default.yml', index)
    process('c', 'conf/default_cpp.yml', index)
    process('c', 'conf/compact.yml', index)
    process('c', 'conf/defines_only.yml', index)
    process('python', 'conf/default.yml', index)


def python():
    process('python', 'conf/default.yml', 'yaml/Intel/index.yml')


def test():
    process('c', TEST_CONFIG, TEST_FILE)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--config',
                        type=str, required=False,
                        default='conf/default.yml',
                        help='Configuration file')

    parser.add_argument('-f', '--file',
                        type=str, required=True,
                        help='YAML file to process')

    parser.add_argument('-p', '--processor',
                        type=str, default='c', required=True,
                        choices=['c', 'python'],
                        help='Processor type')

    args = parser.parse_args()
    process(args.processor, args.config, args.file)


if __name__ == '__main__':
    if ALL:
        process_all()
    elif PYTHON:
        python()
    elif TEST:
        test()
    else:
        main()
