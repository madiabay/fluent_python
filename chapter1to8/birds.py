class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('quack!')


def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck):
    birdie.quack()

def alert_bird(birdie: Bird):
    birdie.quack()