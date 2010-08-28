#!/bin/sh

rpm_run_post() {
     rpm -q --qf "%{POSTIN}" $1 > t.sh
     sh t.sh >> /var/log/post.log 2>&1
     rm t.sh
}

rpm_run_pre() {
    rpm -q --qf "%{PREIN}" $1 > t.sh
    sh t.sh >> /var/log/pre.log 2>&1
    rm t.sh
}

#ͨ�� rpm �ű�����
#/sbin/depmod -a  
/sbin/ldconfig

#���� rpm �ű�����
for i in  ncurses-libs pam rsyslog ; do
    rpm_run_pre $i || :
    rpm_run_post $i || :
done

# Fix /etc/inittab at MI Windows.py.
/bin/sed -i s/id:.:initdefault/id:5:initdefault/ /etc/inittab

#�رղ���Ҫ����
chkconfig --level 2345 dhcpd off
chkconfig --level 2345 dhcrelay off
chkconfig --level 2345 network on
chkconfig --level 234 wine off
chkconfig --level 2345 smb off
#�����û�Ȩ��
chmod 755 /etc/X11 -R
#chmod 755 /etc/kde -R
chmod 755 /usr/{lib,include,share}
#����CD�汾�Զ���������
/sbin/chkconfig --add haldaemon
#������ͨ�û���������
#/usr/sbin/useradd -u 58 -d / -s /sbin/nologin -c "Haldeamon User" -M haldaemon
groupadd plugdev
/usr/sbin/addplug
#����Ĭ��fbsplash����
#���� KDM
echo "DESKTOP=KDE4" > /etc/sysconfig/desktop
echo "DISPLAYMANAGER=KDE4" >> /etc/sysconfig/desktop
echo "Thank you for using MagicInstaller!"
