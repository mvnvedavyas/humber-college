from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController

class SnowflakeTopo(Topo):
    "Snowflake topology with a hub switch and 4 spokes."
    def build(self):
        hub = self.addSwitch('s0')
        spoke1 = self.addSwitch('s1')
        spoke2 = self.addSwitch('s2')
        spoke3 = self.addSwitch('s3')
        spoke4 = self.addSwitch('s4')
        s1host1 = self.addHost('h1', ip='10.0.1.1/24')
        s1host2 = self.addHost('h2', ip='10.0.1.2/24')
        s1host3 = self.addHost('h3', ip='10.0.1.3/24')
        s2host1 = self.addHost('h1', ip='10.0.2.1/24')
        s2host2 = self.addHost('h2', ip='10.0.2.2/24')
        s2host3 = self.addHost('h3', ip='10.0.2.3/24')
        s3host1 = self.addHost('h1', ip='10.0.3.1/24')
        s3host2 = self.addHost('h2', ip='10.0.3.2/24')
        s3host3 = self.addHost('h3', ip='10.0.3.3/24')
        s4host1 = self.addHost('h1', ip='10.0.4.1/24')
        s4host2 = self.addHost('h2', ip='10.0.4.2/24')
        s4host3 = self.addHost('h3', ip='10.0.4.3/24')
        self.addLink(hub, spoke1)
        self.addLink(hub, spoke2)
        self.addLink(hub, spoke3)
        self.addLink(hub, spoke4)
        self.addLink(spoke1, s1host1)
        self.addLink(spoke1, s1host2)
        self.addLink(spoke1, s1host3)
        self.addLink(spoke2, s2host1)
        self.addLink(spoke2, s2host2)
        self.addLink(spoke2, s2host3)
        self.addLink(spoke3, s3host1)
        self.addLink(spoke3, s3host2)
        self.addLink(spoke3, s3host3)
        self.addLink(spoke4, s4host1)
        self.addLink(spoke4, s4host2)
        self.addLink(spoke4, s4host3)

if __name__ == '__main__':
    topo = SnowflakeTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    CLI(net)
    net.stop()
