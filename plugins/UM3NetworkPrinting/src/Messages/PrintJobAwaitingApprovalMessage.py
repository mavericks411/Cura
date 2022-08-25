# Copyright (c) 2022 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices

from UM import i18nCatalog
from UM.Message import Message


I18N_CATALOG = i18nCatalog("cura")


class PrintJobPendingApprovalMessage(Message):
    """Message shown when waiting for approval on an uploaded print job."""

    def __init__(self) -> None:
        super().__init__(
            text = I18N_CATALOG.i18nc("@info:status", "You will receive a confirmation via email when the print job is approved"),
            title=I18N_CATALOG.i18nc("@info:title", "The print job was successfully submitted"),
            message_type=Message.MessageType.POSITIVE
        )
        self.addAction("manage_print_jobs", I18N_CATALOG.i18nc("@action", "Manage print jobs"), "", "")

        self.addAction("learn_more", I18N_CATALOG.i18nc("@action", "Learn more"), "", "",
                        button_style = Message.ActionButtonStyle.LINK,
                        button_align = Message.ActionButtonAlignment.ALIGN_LEFT)

        self.actionTriggered.connect(self._onActionTriggered)

    def _onActionTriggered(self, message: Message, action: str):
        """ Callback function for the "Manage print jobs" button on the pending approval notification. """
        match action:
            case "manage_print_jobs":
                QDesktopServices.openUrl(QUrl("https://ultimaker.com/"))
            case "learn_more":
                QDesktopServices.openUrl(QUrl("https://ultimaker.com/"))
