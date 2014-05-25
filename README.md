telehack
========

Inaugural Telehack


butts

After a reboot, you need to re-set the iptables junk:

```
sudo iptables -A INPUT -p icmp --icmp-type 8 -j LOG --log-prefix "[ping-hammer]"
```

To run the ping listener:

```
cd ~/telehack/ballPing
sudo ./ping-listener

```
