class Nike():
    def __init__(self):
        print('nike')


class Addidas():
    def __init__(self):
        print('addidas')


class Factory():
    def shoes(self, name):
        if name == 'nike':
            return Nike()
        if name == 'addidas':
            return Addidas()


a = Factory().shoes('nike')
b = Factory().shoes('addidas')
