buffer = open('input.txt', 'r').read().strip()


def find_marker(buffer, marker_len):
    for i in range(len(buffer)-marker_len):
        if len(set(buffer[i:i+marker_len])) == marker_len:
            return i+marker_len

pkt_len= 4
print('packet marker ends at:', find_marker(buffer, pkt_len))

msg_len = 14
print('message marker ends at:', find_marker(buffer, msg_len))