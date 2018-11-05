import abc
import collections
import signal
import threading
import time
from typing import NoReturn, Optional

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import AppIndicator3, GLib, Gtk

from indicator_applet.indicator import Indicator, Category, Status


class Applet(abc.ABC):

    """A simple way to create an indicator applet.

    Subclass, then override __init__, do_update, and schedule_update.
    """

    def __init__(self, applet_id: str, icon_name: str = "", category: Category = Category.OTHER, path: Optional[str] = None) -> None:
        self.items = collections.OrderedDict()
        self.indicator = Indicator(applet_id, icon_name, category, path)
        self.indicator.menu = Gtk.Menu()
        self.indicator.status = Status.ACTIVE
        self.update_interval = 1

    def update_loop(self) -> None:
        while True:
            self.schedule_update()
            time.sleep(self.update_interval)

    def schedule_update(self) -> None:
        GLib.idle_add(self.do_update)

    def do_update(self) -> None:
        assert threading.current_thread() is threading.main_thread()

    def handle_quit(self, source) -> NoReturn:
        Gtk.main_quit()

    def run(self) -> NoReturn:
        for name, item in self.items.items():
            self.indicator.menu.append(item)
            if hasattr(self, f"handle_{name}"):
                item.connect("activate", getattr(self, f"handle_{name}"))
        self.indicator.menu.show_all()
        self.update_thread = threading.Thread(target=self.update_loop)
        self.update_thread.daemon = True
        self.update_thread.start()
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        Gtk.main()
