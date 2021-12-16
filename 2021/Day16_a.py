
# Read in stuff
with open("files/input_16.txt", "r") as file_stream:
    line = file_stream.readline()[:-1]
    binary_string = ''.join(list(map(lambda x: bin(int(x, 16))[2:].zfill(4), line)))


def parse_packets(binary):
    version = int(binary[:3], 2)
    s_type = int(binary[3:6], 2)
    if s_type == 4:
        # Literal
        rest = binary[6:]
        i = 0
        num_binary = ""
        while rest[i] == "1":
            num_binary += rest[i+1:i+5]
            i += 5
        num_binary += rest[i + 1:i + 5]
        literal = int(num_binary, 2)
        return (version, s_type, literal), i + 6 + 5
    else:
        # Operator
        l_type = binary[6]
        sub_packets = []
        if l_type == "0":
            total_length_sub_packets = int(binary[7:22], 2)
            rest = binary[22:]
            i = 0
            while i < total_length_sub_packets:
                sub_packet, length = parse_packets(rest[i:])
                i += length
                sub_packets.append(sub_packet)
            return(version, s_type, sub_packets), i + 7 + 15
        else:
            amount_sub_packets = int(binary[7:18], 2)
            rest = binary[18:]
            i = 0
            while len(sub_packets) < amount_sub_packets:
                sub_packet, length = parse_packets(rest[i:])
                i += length
                sub_packets.append(sub_packet)
            return (version, s_type, sub_packets), i + 7 + 11


def count_version_numbers(structure):
    count = structure[0]
    if structure[1] != 4:
        for operation in structure[2]:
            count += count_version_numbers(operation)
    return count


struct, length = parse_packets(binary_string)
print(count_version_numbers(struct))
