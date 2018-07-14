

test = '''Task Switched — Allows the saving of the x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4
context on a task switch to be delayed until an x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction is
actually executed by the new task. The processor sets this flag on every task switch and tests it when
executing x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

  - If the TS flag is set and the EM flag (bit 2 of CR0) is clear, a device-not-available exception (#NM) is
    raised prior to the execution of any x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction; with the
    exception of PAUSE, PREFETCHh, SFENCE, LFENCE, MFENCE, MOVNTI, CLFLUSH, CRC32, and POPCNT.

  - If the TS flag is set and the MP flag (bit 1 of CR0) and EM flag are clear, an #NM exception is not raised
    prior to the execution of an x87 FPU WAIT/FWAIT instruction.

  - If the EM flag is set, the setting of the TS flag has no effect on the execution of x87
    FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

    The processor does not automatically save the context of the x87 FPU, XMM, and MXCSR registers on a
    task switch. Instead, it sets the TS flag, which causes the processor to raise an #NM exception whenever
    it encounters an x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction in the instruction stream for the
    new task (with the exception of the instructions listed above).

    The fault handler for the #NM exception can then be used to clear the TS flag (with the CLTS instruction)
    and save the context of the x87 FPU, XMM, and MXCSR registers. If the task never encounters an x87
    FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction, the x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4
    context is never saved.'''


def make_paragraphs(text):
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


def wrap_justify(text, width, threshold=0.8):
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

    result = leading_spaces     # This variable holds result.
    space_width_list = [ 0 ]    # This list holds width of each space.
    word_index = 0              # This variable holds current word index.
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


def wrap_paragraph(text, width=80, justify=False):
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
                line = wrap_justify(line.rstrip(), width)
            line_list.append(line.rstrip())
            line = leading_spaces + word + ' '
        else:
            line += word + ' '

    if line.rstrip():
        if justify:
            line = wrap_justify(line.rstrip(), width)
        line_list.append(line.rstrip())
    return line_list if line_list else ['']


def wrap(text, width=80):
    result = []
    paragraph_list = make_paragraphs(text)
    for paragraph in paragraph_list:
        line_list = wrap_paragraph(paragraph, width)
        result.extend(line_list)

    return result


def main():
    result = wrap(test, 80)
    result = wrap_justify('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaa', 80)

    i = 0

    for line in result:
        print(line)


if __name__ == '__main__':
    main()

