---
layout: post
title: "考试倒计时的小程序"
date: 2013-01-09 03:02
comments: true
categories: Python
---

# 前言

这是当年考GRE的时候做的一个倒计时的工具。现在想想其实不应该花掉这么多时间去做这么简单的一个倒计时软件的小程序的。
但是以我当时的状态而言的话，其实也没有什么的太好的方法，回到当时那个时间点上我还是会一头栽进去。这个的本质原因在于自己。
在于自己的自律。换句话说，倒计时程序啦，买书啦，和G友一起自习啦，其实都没啥直接作用。
最最重要的作用在于你自己的努力！或者更加准确的说法是个人的自制力。

<!--more-->

比如，我现在的状态就很该反省。其实我对自己说了，我要早点休息的，但是事实上我还是睡觉睡得很晚。一直到了现在，其实归根到底就是我爸爸和我妈妈说的，你没办法控制自己！

控制自己！这个才是关键。

今天一个同学说，你又胖了，其实我一直在自己安慰自己，那个生活不规律，吃得也不是很规律等等，不应该变胖吧。
其实就是自己麻醉自己，自己开脱自己。

自己的基因不是那种怎么吃都不会变胖的人，自己的智商也不是那么的超过别人。

所以你不锻炼就要变胖，你一不认真学习就要落后！这个是没有办法改变的。

几点改进：

* 要知道好丑，什么该做，什么不该做。何时休息何时工作，何时去追求新的目标
* 要有目标谈不上要多么多么伟大，至少不要虚度光阴。游戏什么的当时很爽，但是过后呢？我希望可以得到长久的愉悦！
* 要有执行力，自制力！如果你控制不了你自己你就得完蛋，你就活该是个被别人看不起的人。其实你自己知道是不是！

# 总结

好了，说了这么多其实是我在反思自己的得失和GRE得到的经验教训，其实有的时候天作之合可能就在你的吊儿郎当中被毁灭了。

你必须控制利用好电脑而不是被利用控制！

你必须利用控制好自己的小说阅读欲望而不是被控制！

你必须控制好自己的嘴巴和情绪，如果你没有办法改变，那就闭嘴，慢慢努力！

# 程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

from datetime import datetime
from datetime import timedelta

class HelloWorld:

    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.
    def hello(self, widget, data=None):
        print "时间！"
        print " - 考试倒计时：%s 天" % (outtime-datetime.now()).days
        print " - 已复习天数：%s 天" % (datetime.now()-intime).days
        print " -  38 日：%s (距离  25 日：%3s 天)" % cd(38)
        print " -  31 日：%s (距离  25 日：%3s 天)" % cd(31)
        print " -  24 日：%s (距离  25 日：%3s 天)" % cd(24)
        print " -  17 日：%s (距离  10 日：%3s 天)" % cd(17)
        print " -   5 日：%s (距离   5 日：%3s 天)" % cd(5)



    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    def destroy(self, widget, data=None):
        print "努力！"
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # When the window is given the "delete_event" signal (this is given
        # by the window manager, usually by the "close" option, or on the
        # titlebar), we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        self.window.connect("delete_event", self.delete_event)

        # Here we connect the "destroy" event to a signal handler.
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)

        # Sets the border width of the window.
        self.window.set_border_width(50)

        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("为人生苦战一回！出国，出国，出国！")

        # When the button receives the "clicked" signal, it will call the
        # function hello() passing it None as its argument.  The hello()
        # function is defined above.
        self.button.connect("clicked", self.hello, None)

        # This will cause the window to be destroyed by calling
        # gtk_widget_destroy(window) when "clicked".  Again, the destroy
        # signal could come from here, or the window manager.
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

        # This packs the button into the window (a GTK container).
        self.window.add(self.button)

        # The final step is to display this newly created widget.
        self.button.show()

        # and the window
        self.window.show()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it

intime = datetime(2012,7,5)
outtime = datetime(2012,8,17)

def cd(d):
  tod = outtime - timedelta(d)
  tods = tod - datetime.today()
  return (tod.date(),tods.days)

if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()

raw_input("Press Enter to continue...")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 效果

![tu1](/images/Python/GRETiming/1.png) 

![tu2](/images/Python/GRETiming/2.png) 


其实我看着有要哭的感觉，原来150多天过去了。

你知道时间的流逝了么？

后悔么？

心痛么？

那就好好努力去！
