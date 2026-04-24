from mininet.topo import Topo

class PacketLoggerTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')

        # Dynamically create hosts
        for i in range(1, 5):
            host = self.addHost(f'h{i}')
            self.addLink(host, switch)

# Register topology
topos = {'packetlog': (lambda: PacketLoggerTopo())}