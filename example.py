from pybtclib.wallet import Wallet


if __name__ == '__main__':
    wallet = Wallet()
    # wallet.private_key_hex = '0000000000000000000000000000000000000000000000000000000000000002'
    # wallet.compressed_wif = 'KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU74NMTptX4'
    wallet.uncompressed_wif = '5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAvUcVfH'
    wallet.str_detail()
    # wallet.json_detail()
