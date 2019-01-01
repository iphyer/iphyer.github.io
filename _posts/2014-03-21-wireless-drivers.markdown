---
layout: post
title: "Linux下无线驱动的安装"
date: 2014-03-21 21:03
comments: true
categories: Linux 
---

# 无线驱动安装更新

我发现再从换了新的电脑，就从来没有正常使用过无线驱动。非常郁闷。今天因为觉得无法再拖延了，到了教学楼总是需要使用无线的，所以花了一个晚上的时间Google了一会解决方法，现在总结如下。

<!--more-->

## 查看自己的无线网卡类型

`lspci | grep Network`

输出的结果是

`04:00.0 Network controller: Ralink corp. RT3290 Wireless 802.11n 1T/1R PCIe`

剩下的问题就是google这个型号的网卡和Linux作为关键词看这是不是在Ubuntu的支持中。

参看这个网址给出了正确的使用方法[How do I install ra3290.bin wireless driver into /lib/firmware](http://askubuntu.com/questions/240553/how-do-i-install-ra3290-bin-wireless-driver-into-lib-firmware)

其实Linux内核3.6之后就支持Ra3290了，但是但疼的是我当年是直接从Ubuntu12.04LTS的第一个版本直接安装的。到现在两年了都是3.2的内核。坑爹呢。

有人给出的方法是升级版本，比如14.04这是下一个LTS。但是当年装12.04其实主要目的就是不要升级了，这么升级很麻烦而且其实我用不到很多Ubuntu越来越偏向平板电脑操作的东西，比如Unity桌面。

所以[How do I install RALink 3290?](http://askubuntu.com/questions/226381/how-do-i-install-ralink-3290)上面给出的方案其实非常方便，就是先按更新内核在安装一个无线网卡驱动。

## 升级Ubuntu内核

[给Ubuntu 13.04, 12.10, 12.04以及Linux Mint 15, 14, 13升级最新的内核](http://tweetyf.org/2013/05/upgrade_kernel_ubuntu_limuxmint.html)当然他的版本安装的特别新，本着稳定第一的原则我之选择了3.8的内核。

下载你需要的内核版本，这里特别需要强调要4下载deb格式文件:
安装kernell 3.x.x from [kernel.ubuntu](http://kernel.ubuntu.com/~kernel-ppa/mainline)
比如：

	linux-headers-3.6.6-030606-generic_3.6.6-030606.201211050512_amd64.deb
	linux-headers-3.6.6-030606_3.6.6-030606.201211050512_all.deb
	linux-image-3.6.6-030606-generic_3.6.6-030606.201211050512_amd64.deb	
	linux-image-extra-3.6.6-030606-generic_3.6.6-030606.201211050512_amd64.deb

然后用sudo安装如下命令

```bash
dpkg -i *.deb
update-grub
```

## 下载相应驱动

```bash
git clone git://git.kernel.org/pub/scm/linux/kernel/git/dwmw2/linux-firmware.git
sudo cp linux-firmware/rt3290.bin /lib/firmware
```

### 重启搞定

