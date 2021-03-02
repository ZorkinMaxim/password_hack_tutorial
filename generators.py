class BaseGenerator:
    def reset(self):
        raise NotImplementedError

    def generate(self):
        raise NotImplementedError


class ListGenerator(BaseGenerator):
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0

    def reset(self):
        self.i = 0

    def generate(self):
        if self.i >= len(self.tokens):
            return
        password = self.tokens[self.i]
        self.i += 1
        return password


class FileLinesGenerator(ListGenerator):
    def __init__(self, filename='bad_passwords.txt'):
        with open(filename) as f:
            content = f.read()
        tokens = content.split('\n')
        super().__init__(tokens=tokens)


class BasicLoginsGenerator(ListGenerator):
    def __init__(self):
        super().__init__(tokens=['admin', 'jack', 'cat', 'olga'])


class BruteForceGenerator:
    def __init__(self, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
        self.alphabet = alphabet
        self.base = len(alphabet)
        self.i = 0
        self.length = 0

    def reset(self):
        self.i = 0
        self.length = 0

    def generate(self):
        result = ''
        temp = self.i
        while temp > 0:
            rest = temp % self.base
            result = self.alphabet[rest] + result
            temp = temp // self.base

        while len(result) < self.length:
            result = self.alphabet[0] + result

        if result == self.alphabet[-1] * self.length:
            self.length += 1
            self.i = 0
        else:
            self.i += 1

        return result
