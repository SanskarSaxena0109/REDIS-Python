from database import Database

class CommandRouter:
    def __init__(self,db:Database):
        self.db=db

    def execute(self,command_parts:list):
        if not command_parts:
            return "-ERR empty command"

        cmd=command_parts[0].upper()
        args=command_parts[1:]

        if cmd=="PING":
            if args:
                return args[0]
            return "+PONG"
        elif cmd=="SET":
            if(len(args)<2):
                return "-ERR wrong number of arguments for 'SET' command"
            return self.db.set(args[0],args[1])        

        elif cmd=="GET":
            if(len(args)<1):
                            return "-ERR wrong number of arguments for 'SET' command"
            return self.db.get(args[0])
        elif cmd=="DEL":
            if(len(args)<1):
                            return "-ERR wrong number of arguments for 'SET' command"
            return self.db.delete(args[0])
        elif cmd=="EXISTS":
            if(len(args)<1):
                            return "-ERR wrong number of arguments for 'SET' command"
            return self.db.exists(args[0])

        else:
            return f"-ERR unknown command '{cmd}'or incorrect arguments"