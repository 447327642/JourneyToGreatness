# Thumbtack simple database
import sys
from collections import defaultdict

"""
save value as list(stack) instead of value, so we can handle transaction, each command in transcation


Or:
Add a transcation db, each data command if in transcation db, only modify transcation db (a part or origin db, 
for example, SET a in a transaction, get a value from origin db to transcation db and modify it, if embeded another
transcation, do it recursively)
"""

class SimpleDatabase():
    def __init__(self):
        self._db = defaultdict(int)
        self._num_eq = defaultdict(int)
        
        self._trans = [{}]
        self._db_cache = defaultdict(int)
        self._num_eq_cache = defaultdict(int)


    # ---------------- Data commands ----------------
  
    def exec_data_cmd(self, cmd):
        oper, args = cmd[0], cmd[1:]
        CMD_TAB = {"SET": self.set_val,
                   "GET": self.get_val,
                   "UNSET": self.unset_val,
                   "NUMEQUALTO": self.num_eq,                   
                    }
        CMD_TAB[oper](args)
    
    def set_val(self, args):
        name, val = args[0], int(args[1])
        if self._trans:
            if name in self._db:
                self._num_eq[self._db[name]].append(self._num_eq[self._db[name]][-1] - 1)
            self._db[name] = .append(int(val))
            self._num_eq[val].append()
        else:
            if name in self._db:
                self._num_eq[self._db[name]] -= 1
            self._db[name] = int(val)
            self._num_eq[val] += 1
        return

    def get_val(self, args):
        name = args[0]
        if name not in self._db:
            print "NULL"
        else:
            print (self._db[name])
        return

    def unset_val(self, args):
        name = args[0]
        if name not in self._db:
            return
        self._num_eq[self._db[name]] -= 1 if self._db[name] > 0 else 0
        del self._db[name]
        return 

    def num_eq(self, args):
        val = int(args[0])
        print (self._num_eq[val])
        return

    # ---------------- Transaction commands ----------------
    
    def exec_trans_cmd(self, cmd):
        oper = cmd[0]
        CMD_TAB = {"BEGIN": self.begin,
                   "ROLLBACK": self.rollback,
                   "COMMIT": self.commit,                   
                  }
        CMD_TAB[oper]()
        
        
    def begin(self):
        self._trans.append([])

    def rollback(self):
        pass
    
    def commit(self):
        pass

    def apply_trans(self)




    
DATA_NUM_ARGS = {"SET": 2, "UNSET": 1, "NUMEQUALTO": 1, "GET": 1, "END": 1}
TRANS_NUM_ARGS = {"BEGIN": 0, "ROLLBACK": 0, "COMMIT": 0}

def check_cmd(cmd):
    oper, num_args = cmd[0], len(cmd[1:])
    if oper in DATA_NUM_ARGS.keys():
        if oper not in DATA_NUM_ARGS[num_args]:
            return "UNKNOWN COMMAND"
        else:
            return "DATA COMMAND"
    if oper in TRANS_NUM_ARGS.keys():
        if oper not in TRANS_NUM_ARGS[num[num_args]]:
            return "UNKNOWN COMMAND"
        else:            
            return "TRANS COMMAND"
    if oper == "END":
        return "END"
    else:
        return "UNKNOWN COMMAND"

    
        

def help():
    print ('''
    Data Commands: 
        SET name value
        UNSET name
        NUMEQUALTO value
        END

    Transaction Commands:
       BEGIN
       ROLLBACK
       COMMIT    
    ''')


def main():
    db = SimpleDatabase()
    # CMD_NUM_ARGS = defaultdict(set())
    # for data_cmd in DATA_ARGS:
    #     CMD_NUM_ARGS[data_cmd[1]].add(data_cmd[0])
    # for trans_cmd in TRANS_ARGS:
    #     CMD_NUM_ARGS[trans_cmd[1]].add(trans_num[0])
    while True:
        try:
            cmd = raw_input().split()
        except EOFError:
            sys.exit(1)
        if len(cmd) < 1:
            continue
        cmd[0] = cmd[0].upper()
        
        judge = check_cmd(cmd)
        if judge == "UNKNOWN COMMAND":
            print ("Unknown command")
        elif judge == "END":
            return True
        elif judge == "DATA COMMAND":
            db.exec_data_cmd(cmd)
        elif judge == "TRANS COMMAND":
            db.exec_trans_cmd(cmd)

if __name__ == '__main__':
    main()
