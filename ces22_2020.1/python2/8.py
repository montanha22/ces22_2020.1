from random import random
import abc

class GameObject:
    ''' Visible objects on game screen'''
    dt = 1

    def __init__(self, start_pos = [0, 0], start_velocity = [1, 5]):
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.vx = start_velocity[0]
        self.vy = start_velocity[1]
    
    # Our abstract method, all GameObjects derivated classes must implement it
    @abc.abstractmethod
    def move(self):
        raise NotImplementedError
    
    @staticmethod
    def is_game_object(object):
        return isinstance(object, GameObject)

class Hero(GameObject):
    ''' Our Hero class. It is a GameObject and must overwrite the move method'''
    def __init__(self, hero_start_pos = [0, 0]):
        super().__init__(start_pos = hero_start_pos)
    
    def move(self):
        last_pos = (self.x, self.y)

        self.x = self.x + self.vx * self.dt
        self.y = self.y + self.vy * self.dt

        print('hero moved from {} to {}'.format(last_pos, (self.x, self.y)))

class Enemy(GameObject):

    ''' Our enemy class. It is also a GameObject and must overwrite the move method'''
    enemy_list = []

    def __init__(self, enemy_start_pos = [0, 0]):
        super().__init__(start_pos = enemy_start_pos)
        #print(self.position)
        self.enemy_list.append(self)

    def move(self):

        random_scalar = int (random() * 10 + 1)
        last_pos = (self.x, self.y)
    
        self.x = self.x + random_scalar * self.vx * self.dt
        self.y = self.y + random_scalar * self.vy * self.dt
        
        print('enemy moved from {} to {}'.format(last_pos, (self.x, self.y)))

    # Our class method
    @classmethod
    def get_enemy_list(cls):
        return cls.enemy_list


print('\nCreating GameObject object')
obj = GameObject()
print('trying to make it move')
# can't run move method of GameObject object because its not implemented
try:
    obj.move()
except:
    print('GameObject object can\'t move because move is a abstract method\n')

print('Creating a Hero object (derivated from GameObject)')
hero = Hero([5, 5])
print('Trying to make it move')
hero.move()
print()

print('Creating 2 Enemy objects (derivated from GameObject)')
enemy1 = Enemy()
enemy2 = Enemy()
print('Making them move')
enemy1.move()
enemy2.move()
print()


print('getting a class variable through a class method')
print(Enemy.get_enemy_list())
print()

print('lets see if some objects are GameObject\'s instance using a static method')
objetos = [enemy1, 'enemy', enemy2, 'player', hero, 42]
isgameobject = list(map(GameObject.is_game_object, objetos))
tupled = list(zip(isgameobject, objetos))
for t in tupled:
    print('\t',t)