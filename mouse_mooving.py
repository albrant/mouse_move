import pyautogui


def square_mouse_moving():
    steps = (
        (100, 100),
        (500, 100),
        (500, 500),
        (100, 500),
            )
    for i in range(10):
        for step in steps:
            pyautogui.moveTo(step, duration=0.4)
    print('Завершено')


def scrolling(number_of_scrolling):
    pyautogui.move(0, 200)
    scroll_distance = 800
    for i in range(number_of_scrolling):
        pyautogui.scroll(scroll_distance)
        scroll_distance *= -1
        print(i)


if __name__ == '__main__':
    print('''Для остановки программы нужно
          курсор мыши поместить в угол экрана''')
    print('Начало работы через ', end='')
    pyautogui.countdown(5)
    try:
        # square_mouse_moving()
        scrolling(10)
    except pyautogui.FailSafeException:
        print('Остановка программы')
