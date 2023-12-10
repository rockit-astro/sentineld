## Sentinel proxy daemon

`sentinel` is a Pyro frontend that proxies queries weather and roof state from the Sentinel API.

### Software setup
After installing the package, the systemd service should be enabled:
```
sudo systemctl enable --now sentineld.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9008/tcp --permanent
sudo firewall-cmd --reload
```
