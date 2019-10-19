# Write Memory

## Current Status of Development

This project is currently still in **VERY EARLY** stages of development. Essential files are still being written, and this software is currently still **NOT FUNCTIONING**.

## Description

Write Memory is a Cisco-like utility to write configurations in Linux kernel to persistent configuration files.

## Modules

Write Memory will support a wide ranges of Linux modules in the future, including *iproute2*, *Netfilter* and more.

Currently, Write Memory supports only *iproute2* for developments and experiments.

### iproute2

Supported objects:

- address
- route
- rule
- neigh

```shell
# display configurations
write-memory --show ip address

# write configurations
write-memory --write ip address
```

---

## License

Licensed under the GNU General Public License Version 3 (GNU GPL v3)
https://www.gnu.org/licenses/gpl-3.0.txt

![GPLv3 Icon](https://www.gnu.org/graphics/gplv3-127x51.png)

(C) 2019 K4YT3X

## Special Thanks

Appreciations given to the following code contributors:

- Mark Shtern
