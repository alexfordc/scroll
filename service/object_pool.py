__author__ = 'ict'

import os
import threading

import DAL.file

type_offset = 0
size_offset = 1
lock_offset = 2

success_msg = "Success"
locked_msg = "Object locked"


class ObjectPool:
    def __init__(self, dump_file, save_dir):
        self.dump_file = dump_file
        self.save_dir = save_dir
        self.obj = {}
        self.mutex = threading.Lock()
        if self.save_dir[-1] != os.path.sep:
            self.save_dir += os.path.sep
        if not os.path.isdir(self.save_dir):
            raise Exception("Invalid save directory")
        self.load()
        self.check()

    def load(self):
        if not os.path.exists(self.save_dir + self.dump_file):
            self.obj = {}
        else:
            self.obj = DAL.file.load(self.save_dir + self.dump_file)

    def dump(self):
        DAL.file.save(self.obj, self.save_dir + self.dump_file)

    def lock(self):
        self.mutex.acquire()

    def unlock(self):
        self.mutex.release()

    def filename(self, name):
        return name + "." + self.obj[name][type_offset]

    def check(self):
        remove_list = []
        for name in self.obj:
            if not os.path.exists(self.save_dir + self.filename(name)):
                remove_list.append(name)
        for name in remove_list:
            del self.obj[name]
        self.dump()

    def have_object(self, name):
        self.lock()
        self.check()
        rst = name in self.obj
        self.unlock()
        return rst

    def add_object(self, name, data_type, size):
        self.lock()
        if name in self.obj:
            self.unlock()
            return "Object has exist: " + name
        self.obj[name] = [data_type, int(size), False]
        self.dump()
        self.unlock()
        return success_msg

    def del_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return "No such object named: " + name
        if self.obj[name][lock_offset]:
            self.unlock()
            return locked_msg
        filename = self.filename(name)
        os.remove(self.save_dir + filename)
        del self.obj[name]
        self.unlock()
        return success_msg

    def lock_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return "No such object named: " + name
        if self.obj[name][lock_offset]:
            self.unlock()
            return locked_msg
        else:
            self.obj[name][lock_offset] = True
        self.unlock()
        return success_msg

    def unlock_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return "No such object named: " + name
        if self.obj[name][lock_offset]:
            self.obj[name][lock_offset] = False
            self.unlock()
            return success_msg
        self.unlock()
        return "Object not locked"

    def filename_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return None
        if self.obj[name][lock_offset]:
            self.unlock()
            return None
        filename = self.filename(name)
        self.unlock()
        return filename

    def update_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return
        if self.obj[name][lock_offset]:
            self.unlock()
            return
        self.obj[name][size_offset] = os.path.getsize(self.save_dir + self.filename(name))
        self.unlock()

    def copy_object(self):
        self.lock()
        tmp = self.obj.copy()
        self.unlock()
        return tmp