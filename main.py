from gui import *


def main():
    window = Tk(className='Shape Calc')
    window.geometry("400x200")
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
