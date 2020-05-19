class SuperWeapon(object):

    basedmg = 5

    def __init__(self, addldmg):
        self.basedmg += addldmg

    def dodmg(self, target):
        target.health -= self.basedmg

    def dmgtype(self, dtype):
        return str(dtype)

class weapon(object):

    basedmg = 5

    def __init__(self, addldmg):
        self.basedmg += addldmg

    def dodmg(self, target):
        target.health -= self.basedmg

class SuperSword(weapon):
    
    addldmg = 1000000000000000
    dtype = 'slashing'

    def __init__(self):
        super().__init__(self.addldmg)

    def dodmg(self, target1):
        target1.health = 0

    def dmgtype(self):
        return 'super amazing'

class sword(weapon):
    addldmg = 10
    
    def __init__(self):
        super().__init__(self.addldmg)

    def dodmg(self, target):
        target.health = -1


class Axe(weapon):
    addldmg = 20

    def __init__(self):
        super().__init__(self.addldmg)

class spear(weapon):
    addldmg = 5

    def __init__(self):
        super().__init__(self.addldmg)

class nunchucks(weapon):
    addldmg = 80

    def __init__(self):
        super().__init__(self.addldmg)

class glaive(weapon):
    addldmg = 30

    def __init__(self):
        super().__init__(self.addldmg)

class staff(weapon):
    addldmg = 2

    def __init__(self):
        super().__init__(self.addldmg)







class target(object):
    health = 100

    def __init__(self):
        pass

    def heal(self):
        self.health = 100

mahsword = sword()
mahaxe = Axe()
goblin = target()
mahsword.dodmg(goblin)
mahaxe.dodmg(goblin)
print(goblin.health)