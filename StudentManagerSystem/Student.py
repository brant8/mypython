class Students(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'


if __name__ == '__main__':
    aa = Students('lisi', 'nan', 123456789)
    print(aa)
