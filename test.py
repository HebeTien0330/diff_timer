from controller import Controller, setTimeOut
import pygame

counting = 1

def test():
    global counting
    print(f"test count {counting} done")
    counting += 1
    setTimeOut(test, 2, f"test_{counting}")

def main():
    tick = 1
    flag = 0
    clock = pygame.time.Clock()
    tps = 30
    interval = 5
    controller = Controller()
    controller.initTimer("WHEEL", interval, tps)
    while True:
        clock.tick(tps)
        controller.tick(tick)
        if not flag:
            flag = 1
            setTimeOut(test, 2, f"test_{counting}")
        tick += 1

if __name__ == "__main__":
    main()