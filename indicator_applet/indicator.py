from enum import Enum
from typing import Optional

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk
from gi.repository import AppIndicator3


class Category(Enum):
    APP_STATUS = AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    COMMUNICATIONS = AppIndicator3.IndicatorCategory.COMMUNICATIONS
    SYSTEM = AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
    HARDWARE = AppIndicator3.IndicatorCategory.HARDWARE
    OTHER = AppIndicator3.IndicatorCategory.OTHER


class Status(Enum):
    PASSIVE = AppIndicator3.IndicatorStatus.PASSIVE
    ACTIVE = AppIndicator3.IndicatorStatus.ACTIVE
    ATTENTION = AppIndicator3.IndicatorStatus.ATTENTION


class Indicator:

    def __init__(
        self,
        indicator_id: str,
        icon_name: str,
        category: Category,
        path: Optional[str] = None,
    ) -> None:
        """Create a new indicator.

        Args:
            indicator_id: A unique ID for your indicator.
            icon_name: The name of the icon to use.
            category: What kind of indicator to create.
        """
        if path is None:
            self._indicator = AppIndicator3.Indicator.new(
                indicator_id, icon_name, category.value
            )
        else:
            self._indicator = AppIndicator3.Indicator.new_with_path(
                indicator_id, icon_name, category.value, path
            )

    @property
    def attention_icon(self) -> str:
        return self._indicator.props.attention_icon

    @attention_icon.setter
    def attention_icon(self, icon_name: str):
        self._indicator.props.attention_icon = icon_name

    @property
    def attention_icon_desc(self) -> str:
        return self._indicator.props.attention_icon_desc

    @attention_icon_desc.setter
    def attention_icon_desc(self, icon_desc: str):
        self._indicator.props.attention_icon_desc = icon_desc

    @property
    def category(self) -> Category:
        return Category(self._indicator.get_category())

    @property
    def icon(self) -> str:
        return self._indicator.props.icon_name

    @icon.setter
    def icon(self, icon_name: str):
        self._indicator.props.icon_name = icon_name

    @property
    def icon_desc(self) -> str:
        return self._indicator.props.icon_desc

    @icon_desc.setter
    def icon_desc(self, icon_desc: str):
        self._indicator.props.icon_desc = icon_desc

    @property
    def icon_theme_path(self) -> str:
        return self._indicator.props.icon_theme_path

    @icon_theme_path.setter
    def icon_theme_path(self, icon_theme_path: str):
        self._indicator.props.icon_theme_path = icon_theme_path

    @property
    def id(self) -> str:
        return self._indicator.props.id

    @property
    def label(self) -> str:
        return self._indicator.props.label

    @label.setter
    def label(self, label: str):
        self._indicator.props.label = label

    @property
    def label_guide(self) -> str:
        return self._indicator.props.label_guide

    @label_guide.setter
    def label_guide(self, guide: str):
        self._indicator.props.label_guide = guide

    @property
    def menu(self) -> Gtk.Menu:
        # TODO: is this available via an attribute?
        return self._indicator.get_menu()

    @menu.setter
    def menu(self, menu: Gtk.Menu):
        self._indicator.set_menu(menu)

    @property
    def ordering_index(self) -> int:
        return self._indicator.props.ordering_index

    @ordering_index.setter
    def ordering_index(self, ordering_index: int):
        self._indicator.props.ordering_index = ordering_index

    @property
    def secondary_activate_target(self) -> Optional[Gtk.Widget]:
        return self._indicator.get_secondary_activate_target()

    @secondary_activate_target.setter
    def secondary_activate_target(self, menuitem: Optional[Gtk.Widget]):
        self._indicator.set_secondary_activate_target(menuitem)

    @property
    def status(self) -> Status:
        return Status(self._indicator.get_status())

    @status.setter
    def status(self, status: Status):
        self._indicator.set_status(status.value)

    @property
    def title(self) -> str:
        return self._indicator.get_title()

    @title.setter
    def title(self, title: str):
        self._indicator.set_title(title)
