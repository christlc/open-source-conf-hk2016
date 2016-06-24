# open-source-conf-hk2016
Openwrt talk material

## Slides

Slides are available at:

openwrt_presentation.html

## Code

The Python example can be obtained via serialtest.py


## Firmware 

The firmware is created via the follwoing process

```bash
wget https://downloads.openwrt.org/chaos_calmer/15.05.1/ar71xx/generic/OpenWrt-ImageBuilder-15.05.1-ar71xx-generic.Linux-x86_64.tar.bz2
tar -xvf OpenWrt-ImageBuilder-15.05.1-ar71xx-generic.Linux-x86_64.tar.bz2 
cd OpenWrt-ImageBuilder-15.05.1-ar71xx-generic.Linux-x86_64/
make image PROFILE="TLMR3020" PACKAGES="kmod-fs-ext4 kmod-usb-storage block-mount"
```

The resulting binary is provided openwrt_bin.

