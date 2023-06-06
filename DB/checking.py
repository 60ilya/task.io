class Checking:

    def login_check(login: str):
        length = False
        letters = False
        
        if len(login) >= 6:
            length = True

        for i in login:
            if i.isalpha():
                letters = True

        if length and letters:
            return True
        else:
            return False
        