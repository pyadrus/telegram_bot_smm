from notifypy import Notify
from notifypy.exceptions import UnsupportedPlatform
from rich import print


def app_notifications(notification_text) -> None:
    """
    Выводим уведомление, если операционная система windows 7, то выводим уведомление в консоль
    Библиотека для работы с уведомлениями на разных платформах https://github.com/ms7m/notify-py
    """
    try:
        notification = Notify()
        notification.title = "Telegram_BOT_SMM"
        notification.icon = "system/ico/app_icon.ico"
        notification.application_name = "Telegram_BOT_SMM"
        notification.message = f"{notification_text}"
        notification.send()
    except UnsupportedPlatform:
        print(f"[red] {notification_text}")  # Выводим уведомление
