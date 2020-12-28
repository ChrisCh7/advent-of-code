def main():
    with open('in.txt') as file:
        card_pubkey, door_pubkey = map(lambda n: int(n), file.read().splitlines())

    print('card public key:', card_pubkey)
    print('door public key:', door_pubkey)

    print('card loop size:', card_loop_size := get_loop_size(card_pubkey))
    print('door loop size:', door_loop_size := get_loop_size(door_pubkey))

    print('encryption key:', get_encryption_key(card_loop_size, door_pubkey))


def get_loop_size(pubkey):
    value = 1
    loop_size = 0
    while value != pubkey:
        value *= 7
        value %= 20201227
        loop_size += 1
    return loop_size


def get_encryption_key(first_loop_size, second_public_key):
    value = 1
    loop_size = 0
    while loop_size < first_loop_size:
        value *= second_public_key
        value %= 20201227
        loop_size += 1
    return value


if __name__ == '__main__':
    main()
