from functools import reduce


def part1(message: str):
    message_binary = convert_message_to_binary(message)

    packets = parse_message(message_binary)

    for packet in packets:
        if packet.length_type_id == 0:
            packet.nr_sub_packets = len(packet.sub_packets)

    sum_values = 0

    for packet in packets:
        sum_values += packet.version_nr

    print('Part 1:', sum_values)
    return packets


def part2(packets: list['Packet']):
    print('Part 2:', get_value(packets[0]))


class Packet:
    def __init__(self, version_nr, type_id, length_type_id=-1):
        self.version_nr = version_nr
        self.type_id = type_id
        self.length_type_id = length_type_id
        self.nr_sub_packets = 0
        self.sub_packets = []
        self.literal_value = -1

    def __repr__(self):
        return f'Packet(version_nr={self.version_nr}, type_id={self.type_id}, length_type_id={self.length_type_id}, ' \
               f'nr_sub_packets={self.nr_sub_packets}, sub_packets={self.sub_packets}, literal_value={self.literal_value}) '


def parse_message(message_binary: str):
    packets = []
    parents = []

    while len(message_binary) > 5:
        packet = Packet(int(message_binary[:3], 2), int(message_binary[3:6], 2))
        message_binary = message_binary[6:]

        if packet.type_id == 4:
            value, message_binary = get_literal_value(message_binary)
            packet.literal_value = value
        else:
            packet.length_type_id = int(message_binary[0])
            message_binary = message_binary[1:]

            if packet.length_type_id == 0:
                total_length_subp = int(message_binary[:15], 2)
                message_binary = message_binary[15:]

                if len(message_binary) - total_length_subp < 11:
                    message_binary = message_binary[:total_length_subp]
            else:
                nr_subp = int(message_binary[:11], 2)
                message_binary = message_binary[11:]
                packet.nr_sub_packets = nr_subp

        if packet.type_id == 4 and parents:
            while parents:
                if parents[-1][0].length_type_id == 0 and parents[-1][2] - len(message_binary) <= parents[-1][1]:
                    parents[-1][0].sub_packets.append(packet)
                    break
                elif (parents[-1][0].length_type_id == 1 and
                      len(parents[-1][0].sub_packets) < parents[-1][0].nr_sub_packets):
                    parents[-1][0].sub_packets.append(packet)
                    break
                else:
                    parents.pop()
        elif packet.type_id != 4 and parents:
            while parents:
                if parents[-1][0].length_type_id == 0 and parents[-1][2] - len(message_binary) <= parents[-1][1]:
                    parents[-1][0].sub_packets.append(packet)
                    break
                elif (parents[-1][0].length_type_id == 1 and
                      len(parents[-1][0].sub_packets) < parents[-1][0].nr_sub_packets):
                    parents[-1][0].sub_packets.append(packet)
                    break
                else:
                    parents.pop()
            if packet.length_type_id == 0:
                parents.append([packet, total_length_subp, len(message_binary)])
            else:
                parents.append([packet])
        elif packet.type_id != 4:
            if packet.length_type_id == 0:
                parents.append([packet, total_length_subp, len(message_binary)])
            else:
                parents.append([packet])

        packets.append(packet)

    return packets


def get_literal_value(message: str):
    parts = []
    while True:
        parts.append(message[:5])
        message = message[5:]
        if parts[-1][0] == '0':
            break

    binary_value = ''.join([part[1:] for part in parts])
    value = int(binary_value, 2)

    return value, message


def convert_message_to_binary(message: str):
    message_binary = [bin(int(n, 16)) for n in list(message)]
    message_binary = ''.join([n.lstrip('0b').zfill(4) for n in message_binary])
    return message_binary


def get_value(packet: Packet):
    match packet.type_id:
        case 4:
            return packet.literal_value
        case 0:
            return sum([get_value(p) for p in packet.sub_packets])
        case 1:
            values = [get_value(p) for p in packet.sub_packets]
            return reduce(lambda a, b: a * b, values)
        case 2:
            values = [get_value(p) for p in packet.sub_packets]
            return min(values)
        case 3:
            values = [get_value(p) for p in packet.sub_packets]
            return max(values)
        case 5:
            values = [get_value(p) for p in packet.sub_packets]
            return int(values[0] > values[1])
        case 6:
            values = [get_value(p) for p in packet.sub_packets]
            return int(values[0] < values[1])
        case 7:
            values = [get_value(p) for p in packet.sub_packets]
            return int(values[0] == values[1])


if __name__ == '__main__':
    with open('in.txt') as file:
        message = file.readline()

    packets = part1(message)
    part2(packets)
