#
#  Copyright(C) 2021, Isao Hara, all rights reserved.
#
import nfc
import nfc.tag.tt3
import nfc.tag.tt4
import binascii
import os
import time

#
#  Card Reader
class CardReader(object):
  def __init__(self):
    self.clf=nfc.ContactlessFrontend('usb')
    self.target = None

    self.T106A = nfc.clf.RemoteTarget("106A")
    self.T106B = nfc.clf.RemoteTarget("106B")

    # FeliCa
    self.suica = self.set_felica("0003")
    self.edy = self.set_felica("8054")
    self.express = self.set_felica("854C")
    self.nanaco = self.set_felica("04C7")

    self.targets = [ self.T106A, self.T106B, self.edy, self.express, self.nanaco ]

  #
  #
  def set_felica(self, sys):
    target = nfc.clf.RemoteTarget("212F")
    target.sensf_req=bytearray.fromhex("00%s0000" % sys)
    return target

  #
  #
  def sense(self):
    self.target = self.clf.sense(self.suica, interval=0.2)
    if self.target is None:
      self.target = self.clf.sense(*self.targets, interval=0.2)
    return self.target

  #
  #
  def on_discover(self, target):
    if target is None: return False
    if target.sel_res and target.sel_res[0] & 0x40:
      return False
    elif target.sensf_res and target.sensf_res[1:3] == b"\x01\xFE" :
      return False
    else:
      return True   

  #
  #
  def get_idm(self, tag):
    if bool(tag):
      return binascii.hexlify(tag.identifier).decode()
    return None
 
  #
  #
  def read_card_id(self):
    while self.sense() is None: time.sleep(0.1)
    if self.on_discover(self.target) :
      tag = nfc.tag.activate(self.clf, self.target)
      return tag, self.get_idm(tag)

#
#
def main():
  cr=CardReader()
  print("Please touch")
  tag, idm = cr.read_card_id()
  print(idm, tag)
  

if __name__ == '__main__':
  main()

