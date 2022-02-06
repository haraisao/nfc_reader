# coding:utf-8
import nfc
import binascii

clf = nfc.ContactlessFrontend('usb')
print('touch card:')
try:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
finally:
    clf.close()

idm = binascii.hexlify(tag.identifier).decode()

print(idm)