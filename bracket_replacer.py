def bracket_replacer(text):
    replaced_text = ""

    bracket_depth = 0

    for line in text.splitlines():
        if "\\displaystyle" in line:
            line = line.replace("\\displaystyle","")

            if "\\ \\ \\ \\ \\" in line:
                replaced_text += "\\begin{equation}" + line + " \\end{equation}" + "\n"

            else:
                replaced_text += "\\[" + line + "\\]" + "\n"

        else:
            for char in line:
                replaced_char = ""

                if char not in ("{}"): replaced_char = char

                elif char == "{":
                        bracket_depth += 1
                        replaced_char = "$" if bracket_depth == 1 else "{"

                elif char == "}":
                        bracket_depth -= 1
                        replaced_char = "$" if bracket_depth == 0 else "}"

                else:
                    print(char)
                    print "BADDDDDD"

                replaced_text += replaced_char

        replaced_text += "\n"

    return replaced_text

import sys

input_text = sys.stdin.read()
print(bracket_replacer(input_text))