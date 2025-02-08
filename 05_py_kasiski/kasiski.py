class Caeser :
    def to_lowercase_letter_only(plaintext:str) -> str:
        ret = plaintext.lower()
        return "".join(i for i in ret if ret.isalpha())

    def encrypt(plaintext:str, key:str = None) -> str:
        if key is None:
            return plaintext
        else:
            ret = Caeser.to_lowercase_letter_only(plaintext)
            for i in ret:
                ret = ret.replace(i,i+key)
            return ret

