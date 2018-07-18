from typing import List


class DocTextCase(object):
    #
    # TWO_WORDS -> TwoWords
    #
    @staticmethod
    def to_camel_case(text: str) -> str:
        return ''.join(e.title() for e in text.split('_'))

    #
    # TWO_WORDS -> two_words
    #
    @staticmethod
    def to_snake_case_lower(text: str) -> str:
        return text.lower()

    #
    # TWO_WORDS -> TWO_WORDS
    #
    @staticmethod
    def to_snake_case_upper(text: str) -> str:
        return text


class DocTextWrapper(object):
    @staticmethod
    def to_paragraphs(text: str) -> List[str]:
        paragraph_list = []
        paragraph = ''

        for line in text.splitlines():
            if line:
                if not paragraph:
                    paragraph += line.rstrip()
                else:
                    paragraph += ' ' + line.strip()
            else:
                paragraph_list.append(paragraph)
                paragraph = ''

        if paragraph:
            paragraph_list.append(paragraph)

        return paragraph_list if paragraph_list else ['']

    @staticmethod
    def wrap_justify(text: str, width: int, threshold: float=0.8) -> str:
        if len(text) > width or (len(text) / width) < threshold:
            return text

        #
        # Preserve leading spaces.
        #
        leading_space_count = len(text) - len(text.lstrip(' '))
        leading_spaces = ' ' * leading_space_count

        #
        # Split text and count spaces.
        #
        splitted_text = text.strip().split(' ')
        number_of_spaces = len(splitted_text) - 1

        #
        # Is there at least 1 space?
        #
        if number_of_spaces <= 0:
            return text

        #
        # Compute total length of text without spaces.
        #
        text_length_without_spaces = len(text) - number_of_spaces

        #
        # Compute desirable space width (real number).
        #
        desirable_space_width = (width - text_length_without_spaces) / number_of_spaces

        result = leading_spaces  # This variable holds result.
        space_width_list = [0]  # This list holds width of each space.
        word_index = 0  # This variable holds current word index.
        for word in splitted_text[:-1]:
            result += word

            #
            # If the text starts with '-' or '*', assume this is part of
            # the bullet list and fix the space width to 1.
            #
            if word in ['-', '*'] and word_index == 0:
                result += ' '
                space_width_list[-1] += 1

            #
            # In every other case, append spaces so their average will be
            # close to our desirable space width.
            #
            else:
                while sum(space_width_list) / len(space_width_list) < desirable_space_width:
                    result += ' '
                    space_width_list[-1] += 1

            space_width_list.append(0)

            word_index += 1

        #
        # Append last word.
        #
        result += splitted_text[-1]

        return result

    @staticmethod
    def wrap_paragraph(text: str, width: int=80, justify: bool=False) -> List[str]:
        leading_space_count = len(text) - len(text.lstrip(' '))
        leading_spaces = ' ' * leading_space_count

        splitted_paragraph = text.strip().split(' ')
        line_list = []
        line = leading_spaces
        for word in splitted_paragraph:
            if len(line + word) > width:
                if line == leading_spaces:
                    line += word

                if justify:
                    line = DocTextWrapper.wrap_justify(line.rstrip(), width)
                line_list.append(line.rstrip())
                line = leading_spaces + word + ' '
            else:
                line += word + ' '

        if line.rstrip():
            if justify:
                line = DocTextWrapper.wrap_justify(line.rstrip(), width)
            line_list.append(line.rstrip())
        return line_list if line_list else ['']


class DocText(object):
    @staticmethod
    def convert_case(text: str, letter_case: str) -> str:
        if letter_case == 'camel_case':
            return DocTextCase.to_camel_case(text)
        elif letter_case == 'snake_case':
            return DocTextCase.to_snake_case_lower(text)
        else:  # letter_case == 'snake_case_upper':
            return text

    @staticmethod
    def wrap(text: str, width: int=80, justify: bool=False) -> List[str]:
        result = []
        paragraph_list = DocTextWrapper.to_paragraphs(text)
        for paragraph in paragraph_list:
            line_list = DocTextWrapper.wrap_paragraph(paragraph, width, justify)
            result.extend(line_list)

        return result
