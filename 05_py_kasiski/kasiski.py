class Caeser :
    def to_lowercase_letter_only(plaintext:str) -> str:
        ret = plaintext.lower()
        return "".join(i for i in ret if ret.isalpha())

    def encrypt(plaintext:str, key:str = None) -> str:
        if key is None:
            return Caeser.to_lowercase_letter_only(plaintext)
        else:
            text = Caeser.to_lowercase_letter_only(plaintext)
            ret = ""
            for c in text:
                letter = ord(c) - ord('a')
                shift = ord(key) - ord('a')
                ret += chr(((letter + shift) % 26) + ord('a'))
            return ret

    def decrypt(plaintext:str, key:str = None) -> str:
        if key is None:
            return Caeser.to_lowercase_letter_only(plaintext)
        else:
            text = Caeser.to_lowercase_letter_only(plaintext)
            ret = ""
            for c in text:
                letter = ord(c) - ord('a')
                shift = ord(key) - ord('a')
                ret += chr(((letter - shift + 26) % 26) + ord('a'))
            return ret