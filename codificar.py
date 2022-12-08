#codificando numeros repetidos até 9
#ex: aaaa == 4a
#aaaaaaaaaaaa == 9a3a
def run_length_encode(input_str):
    run_length_encoded_string = []
    current_run_length = 1

    for i in range(1, len(input_str)):
        current_char = input_str[i]
        previous_char = input_str[i-1]
        if current_char != previous_char or current_run_length == 9:
            run_length_encoded_string.append(str(current_run_length))
            run_length_encoded_string.append(previous_char)
            current_run_length = 0
        current_run_length += 1

    run_length_encoded_string.append(str(current_run_length))
    run_length_encoded_string.append(input_str[len(input_str)-1])
    return "".join(run_length_encoded_string)

string = "BBBBBBBBBBBBBAACCCDD"

print(run_length_encode(string))