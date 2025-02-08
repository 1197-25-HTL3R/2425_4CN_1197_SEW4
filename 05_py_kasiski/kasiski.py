class Caeser :
    def to_lowercase_letter_only(plaintext:str) -> str:
        ret = plaintext.lower()
        return "".join(i for i in ret if ret.isalpha())


