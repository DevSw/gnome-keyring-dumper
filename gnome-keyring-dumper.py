#! /usr/bin/env python

# this is inspired by http://blog.schmichael.com/2008/10/30/listing-all-passwords-stored-in-gnome-keyring/
 
import pygtk
pygtk.require('2.0')
import gnomekeyring
 
def hack():
    for keyring in gnomekeyring.list_keyring_names_sync():
        for id in gnomekeyring.list_item_ids_sync(keyring):
            item = gnomekeyring.item_get_info_sync(keyring, id)
            attr = gnomekeyring.item_get_attributes_sync(keyring, id)
            if attr and attr.has_key('username_value'):
                print '[%s] %s: %s = %s' % (
                    keyring,
                    item.get_display_name(),
                    attr['username_value'],
                    item.get_secret()
                )
            else:
                print '[%s] %s = %s' % (
                    keyring,
                    item.get_display_name(),
                    item.get_secret()
            )
        else:
            if len(gnomekeyring.list_item_ids_sync(keyring)) == 0:
                print '[%s] --empty--' % keyring
 
if __name__ == '__main__':
    # the signal handler is needed because of
    # http://stackoverflow.com/questions/16410852/keyboard-interrupt-with-with-python-gtk
    # https://bugzilla.gnome.org/show_bug.cgi?id=622084
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    hack()
