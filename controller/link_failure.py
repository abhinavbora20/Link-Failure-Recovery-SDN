from pox.core import core

import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str

log = core.getLogger()

class LinkFailure(object):

    def __init__(self):
        core.openflow.addListeners(self)
        log.info("✅ Custom Controller Started")

    def _handle_ConnectionUp(self, event):
        log.info("🔌 Switch connected: %s", dpid_to_str(event.dpid))

    def _handle_PortStatus(self, event):
        if event.ofp.desc.state == 1:
            log.info("⚠️ LINK DOWN detected at switch %s", dpid_to_str(event.dpid))
        else:
            log.info("✅ LINK UP at switch %s", dpid_to_str(event.dpid))

    def _handle_PacketIn(self, event):
        # Basic forwarding using FLOOD
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)

def launch():
    core.registerNew(LinkFailure)
