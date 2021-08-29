from aqt import gui_hooks
from PyQt5 import QtWidgets
from aqt.qt import qconnect
from aqt.utils import showInfo
from aqt.addons import AddonsDialog, AddonManager

def addons_dialog_will_show(addons_dialog: AddonsDialog):
    addons_dialog.copiable_addon_list = QtWidgets.QPushButton(addons_dialog)
    addons_dialog.copiable_addon_list.setObjectName("copiableAddonList")
    addons_dialog.form.verticalLayout.addWidget(addons_dialog.copiable_addon_list)
    qconnect(addons_dialog.copiable_addon_list.clicked, show_addon_list(addons_dialog.mgr))
    addons_dialog.copiable_addon_list.setText("Debugging list")

gui_hooks.addons_dialog_will_show.append(addons_dialog_will_show)
def show_addon_list(mgr: AddonManager):
    def aux():
        l = []
        for meta in mgr.all_addon_meta():
            l.append(f"""{meta.human_name()}\t{meta.ankiweb_id()}\t{"enabled" if meta.enabled else "disabled"}\t""")
        showInfo("\n".join(l))
    return aux

    