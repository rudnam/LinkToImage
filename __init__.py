from .link_images import link_images
from aqt import mw, gui_hooks
from aqt.utils import qconnect
from aqt.qt import QAction

config = mw.addonManager.getConfig(__name__)

RUN_AT_SYNC = config["run_at_sync"]

action = QAction("Link to image", mw)

if (RUN_AT_SYNC):
    gui_hooks.sync_did_finish.append(link_images)

qconnect(action.triggered, link_images)
mw.form.menuTools.addAction(action)
