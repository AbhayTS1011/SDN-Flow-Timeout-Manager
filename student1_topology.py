from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink


def run():
    setLogLevel("info")

    net = Mininet(
        switch=OVSSwitch,
        controller=None,
        link=TCLink,
        autoSetMacs=True,
    )

    # Controller (POX default port 6633)
    c0 = net.addController(
        "c0",
        controller=RemoteController,
        ip="127.0.0.1",
        port=6633,
    )

    # Switches
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    # Hosts
    h1 = net.addHost("h1", ip="10.0.0.1/24")
    h2 = net.addHost("h2", ip="10.0.0.2/24")
    h3 = net.addHost("h3", ip="10.0.0.3/24")
    h4 = net.addHost("h4", ip="10.0.0.4/24")
    h5 = net.addHost("h5", ip="10.0.0.5/24")

    # Links
    net.addLink(h1, s1, bw=10)
    net.addLink(h2, s1, bw=10)
    net.addLink(h3, s1, bw=10)

    net.addLink(h4, s2, bw=10)
    net.addLink(h5, s2, bw=10)

    net.addLink(s1, s2, bw=100)

    # Start network
    net.start()

    info("\nNetwork started successfully\n")

    CLI(net)

    net.stop()


if __name__ == "__main__":
    run()
