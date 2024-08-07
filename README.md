# pybtclib
Bitcoin private key conversion and address conversion

## 1.Install pkg

```
# windows pkg
pip install pybtclib-2.1.0-win.tar.gz

# linux pkg
pip install pybtclib-2.1.0-linux.tar.gz
```

## 2.Example usage

```
from pybtclib.wallet import Wallet


if __name__ == '__main__':
    wallet = Wallet()
    # wallet.private_key_hex = '0000000000000000000000000000000000000000000000000000000000000002'
    # wallet.compressed_wif = 'KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU74NMTptX4'
    wallet.uncompressed_wif = '5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAvUcVfH'
    wallet.str_detail()
    # wallet.json_detail()
```

## 3.Program running results:

```
P2PKH(c): 1cMh228HTCiwS8ZsaakH8A8wze1JR5ZsP
P2PKH(u): 1LagHJk2FyCV2VzrNHVqg3gYG4TSYwDV4m
BECH32(c): bc1qq6hag67dl53wl99vzg42z8eyzfz2xlkvxechjp
WIF(c): KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU74NMTptX4
WIF(u): 5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAvUcVfH
HEX: 0000000000000000000000000000000000000000000000000000000000000002
```
