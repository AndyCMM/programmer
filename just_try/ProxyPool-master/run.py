from proxypool.api import app
from proxypool.schedule import Schedule


def main():
    """

    :return:
    """

    s = Schedule()
    s.run()
    app.run()


if __name__ == '__main__':
    main()
    print(main.__doc__)

