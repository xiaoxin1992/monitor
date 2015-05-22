#! /usr/bin/env python

import platform

class OpSysType(object):
    def __getattr__(self,attr):
        if attr == "osx":
            return "osx"
        elif attr == "rhel":
            return "redhat"
        elif attr == "ubu":
            return "Ubunt"
        elif attr == "centos":
            return "Centos"
        else:
            return AttributeError,attr
    def linuxType(self):
        print platform.uname()
        if platform.dist()[0] == "centos":
            return self.centos
        elif platform.uname()[1] == self.ubu:
            return self.ubu
        else:
            return "ok"
    def queryOS(self):
        if platform.system() == "Darwin":
            return self.osx
        elif platform.system() == "Linux":
            return self.linuxType()
print platform.system()
def fing():
    type = OpSysType()
    print type.queryOS()
if __name__ == "__main__":
    fing()
