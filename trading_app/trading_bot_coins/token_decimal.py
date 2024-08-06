
def get_token_decimal(decimal):
    """
    The function takes the numeric value of decimal and returns the name
    :param decimal:
    :return name of the given decimal:
    eg : for decimal =6 mWei is returned
    """
    decimal = int("1" + str("0" * decimal))
    decimals_dict = {"wei": 1,
                    "kwei": 1000,
                    "babbage": 1000,
                    "femtoether": 1000,
                    "mwei": 1000000,
                    "lovelace": 1000000,
                    "picoether": 1000000,
                    "gwei": 100000000,
                    "shannon": 1000000000,
                    "nanoether": 1000000000,
                    "nano": 1000000000,
                    "szabo": 1000000000000,
                    "microether": 1000000000000,
                    "micro": 1000000000000,
                    "finney": 1000000000000000,
                    "milliether": 1000000000000000,
                    "milli": 1000000000000000,
                    "ether": 1000000000000000000,
                    "kether": 1000000000000000000000,
                    "grand": 1000000000000000000000,
                    "mether": 1000000000000000000000000,
                    "gether": 1000000000000000000000000000,
                    "tether": 1000000000000000000000000000000}

    # list out keys and values separately
    key_list = list(decimals_dict.keys())
    val_list = list(decimals_dict.values())

    # print key with val 100
    position = val_list.index(decimal)
    return key_list[position]
