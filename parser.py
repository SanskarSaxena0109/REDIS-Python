class RESPParser:
    @staticmethod
    async def decode(reader):
        line = await reader.readline()
        if not line:
            return None
        
        
        if line.startswith(b"*"):
            try:
                num_elements = int(line[1:].strip())
            except ValueError:
                return []

            elements = []
            for _ in range(num_elements):
                
                len_line = await reader.readline()
                if not len_line.startswith(b"$"):
                    break
                try:
                    length = int(len_line[1:].strip())
                except ValueError:
                    break
                
                
                data_line = await reader.readline()
                if len(data_line) >= 2:
                    
                    elements.append(data_line[:-2].decode("utf-8", errors="ignore"))
                else:
                    elements.append(data_line.decode("utf-8", errors="ignore").strip())
            return elements

       
        return line.decode("utf-8", errors="ignore").strip().split()

    @staticmethod
    def encode(response):
        if isinstance(response,str):
            if response.startswith("+")or response.startswith("-"):
                return f"{response}\r\n".encode("utf-8")
            return f"${len(response)}\r\n{response}\r\n".encode("utf-8")
        elif response is True:
            return "+OK\r\n".encode("utf-8")
        elif isinstance(response,int):
            return f":{response}\r\n".encode("utf-8")

        elif response is None:
            return "$-1\r\n".encode("utf-8")
        
        elif isinstance(response,list):
            encoded=f"*{len(response)}\r\n"
            for item in response:
                encoded+=f"*{len(str(item))}\r\n{len(str(item))}\r\n"
            return encoded.encode("utf-8")

        return "-ERR unknown response type\r\n".encode("utf-8")