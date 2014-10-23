__author__ = 'ict'

import os
import threading
import shutil

import DAL.file

type_offset = 0
size_offset = 1
lock_offset = 2

success_msg = "Success"
locked_msg = "Object locked: "
noexist_msg = "No such object: "
exist_msg = "Object have exist: "
unavilable_msg = "Object unavilable: "


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
        for _, attr in self.obj.items():
            attr[lock_offset] = False

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
        self.dump()
        rst = name in self.obj
        self.unlock()
        return rst

    def avilable_object(self, name):
        self.lock()
        self.check()
        self.dump()
        rst = name in self.obj
        if rst:
            rst = not self.obj[name][lock_offset]
        self.unlock()
        return rst

    def add_object(self, name, data_type, size):
        self.lock()
        if name in self.obj:
            self.unlock()
            return exist_msg + name
        self.obj[name] = [data_type, int(size), False]
        self.dump()
        self.unlock()
        return success_msg

    def del_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        if self.obj[name][lock_offset]:
            self.unlock()
            return locked_msg + name
        filename = self.filename(name)
        os.remove(self.save_dir + filename)
        del self.obj[name]
        self.unlock()
        return success_msg

    def lock_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        if self.obj[name][lock_offset]:
            self.unlock()
            return locked_msg + name
        else:
            self.obj[name][lock_offset] = True
        self.unlock()
        return success_msg

    def unlock_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        if self.obj[name][lock_offset]:
            self.obj[name][lock_offset] = False
            self.unlock()
            return success_msg
        self.unlock()
        return success_msg

    def save_object(self, name, data):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        filename = self.filename(name)
        DAL.file.save(data, self.save_dir + filename)
        self.unlock()
        return success_msg

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
        self.obj[name][size_offset] = os.path.getsize(self.save_dir + self.filename(name))
        self.dump()
        self.unlock()

    def copy_entry_object(self):
        self.lock()
        tmp = self.obj.copy()
        self.unlock()
        return tmp

    def rename_object(self, name, rename):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        if self.obj[name][lock_offset]:
            self.unlock()
            return locked_msg + name
        if rename in self.obj:
            self.unlock()
            return exist_msg + rename
        tmp = self.obj[name].copy()
        src = self.filename(name)
        del self.obj[name]
        self.obj[rename] = tmp
        dst = self.filename(rename)
        os.rename(src, dst)
        self.dump()
        self.unlock()
        return success_msg

    def clone_object(self, name, clonename):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        if self.obj[name][lock_offset]:
            self.unlock()
            return locked_msg + name
        if clonename in self.obj:
            self.unlock()
            return exist_msg + clonename
        self.obj[clonename] = self.obj[name]
        shutil.copyfile(self.save_dir + self.filename(name), self.save_dir + self.filename(clonename))
        self.unlock()
        return success_msg

    def get_object(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        data = DAL.file.load(self.save_dir + self.filename(name))
        self.unlock()
        return data

    def get_type(self, name):
        self.lock()
        if name not in self.obj:
            self.unlock()
            return noexist_msg + name
        rst = self.obj[name][type_offset]
        self.unlock()
        return rst