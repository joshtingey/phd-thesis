from flux import flux
from xsec import xsec
from events import events
from profiles import profiles
from digi import digi
from cvn import cvn


def main():
    flux()
    xsec()
    events()
    profiles()
    digi()
    cvn()


if __name__ == "__main__":
    main()