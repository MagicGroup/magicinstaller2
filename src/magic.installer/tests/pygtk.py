#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import pygtk
#pygtk.require('2.0')
import gtk

class base:
#destroy�źŵĻص�����
        def destroy(self,widget,data=None):
                gtk.main_quit()

#clicked�źŵĻص�����
        def hello(self,widget,data):
                print 'hello ' + data + ' this is a button clicked() test'

#delete_event�¼��Ļص�����
        def delete_event(self, widget, event, data=None):
                print "delete event occurred"
#���delete_event�¼����ؼ٣���ᴥ��destroy�źţ��Ӷ��رմ��ڡ�
#��������棬�򲻻�رմ��ڡ���������ڵ�������Ҫһ��ȷ���Ƿ��˳���ѡ��Ի���ʱ�Ǻ����á�
                return False

        def __init__(self):
                self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#���ô��ڵ�delete_event�źŴ���delete_event����
                self.window.connect("delete_event", self.delete_event)
#���ô��ڵ�destroy�źŴ���destroy����
                handler1 = self.window.connect("destroy",self.destroy)
                print "handler1 is:%d" % handler1
                self.window.set_title('PyGTK ���� window')
                self.window.set_default_size(200,200)
                self.window.set_border_width(100)
#���ƴ��ڳ��ֵ�λ��
                self.window.set_position(gtk.WIN_POS_CENTER)
#���ɰ�ťʵ��
                self.button1 = gtk.Button()
                childimage = self.button1.get_child()
                if childimage != None:
                        childimage.set_from_file('b.gif')
                else:
                        imageb=gtk.Image()
                        imageb.set_from_file('a.gif')
                        #Buttons[i].add(imageb)

                self.button2 = gtk.Button()
                self.button1.set_label('label1')
                self.button2.set_label('label2')
#���ð�ť��clicked�źŴ���hello�����������ݡ�pyGTK���ַ���������hello����
                handler2 = self.button1.connect("clicked",self.hello,"pyGTK")
                print "handler2 is:%d" % handler2
#���ð�ť��clicked�źŴ���self.window�����gtk.Widget.destroy����
                self.button1.connect_object("clicked", gtk.Widget.destroy, self.window)
#ʹ��object.disconnect(id)����ȡ��handler2�Ĺ���
#               self.button.disconnect(handler2)
#����һ�����ɼ��ĺ������λself.box1
                self.box1 = gtk.HBox(False, 0)
#��box1�ŵ�������
                self.window.add(self.box1)
#��button1�����ŵ�box1��
                self.box1.pack_start(self.button1,True,True,0)
                self.button1.show()
#��button2�����ŵ�button1����֮��
                self.box1.pack_start(self.button2,True,True,0)
                self.button2.show()
                self.box1.show()
                self.window.show()

        def main(self):
                gtk.main()

print __name__
if __name__ == "__main__":
        base = base()
        base.main()
