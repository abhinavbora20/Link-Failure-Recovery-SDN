from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class LinkFailure(object):

    def __init__(self):
        core.openflow.addListeners(self)
        log.info("Custom Controller Started")

    def _handle_ConnectionUp(self, event):
        log.info("Switch connected: %s", event.dpid)

    def _handle_PortStatus(self, event):
        if event.ofp.desc.state == 1:
            log.info("⚠️ LINK DOWN detected at switch %s", event.dpid)
        else:
            log.info("✅ LINK UP at switch %s", event.dpid)

def launch():
    core.registerNew(LinkFailure)
