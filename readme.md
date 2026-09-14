# PyRedis 🚀

A lightweight, asynchronous, Redis-compatible in-memory key-value data store built completely from scratch in Python. 

This project implements core database storage, custom network handling, and the **RESP (REdis Serialization Protocol)** wire format, allowing standard tools like `redis-cli` to connect and interact with it seamlessly.

---

## 🏗️ System Architecture

The codebase is modularly structured to separate networking, protocol parsing, command routing, and data persistence:

```text
[redis-cli / Client] 
       │ (TCP / RESP Protocol)
       ▼
  server.py       ──► Handles async networking & client concurrency (asyncio)
       │
       ▼
   parser.py      ──► Decodes raw RESP streams & encodes responses back to wire format
       │
       ▼
   router.py      ──► Validates command syntax, argument counts, and dispatches actions
       │
       ▼
  database.py     ──► In-memory key-value storage engine (RAM-based dictionary)



   📂PROJECT STRUCTURE:
   redis.python/
│
├── server.py       # Asynchronous TCP server socket loop
├── parser.py       # RESP protocol decoder & encoder 
├── router.py       # Command dispatcher and argument validation
└── database.py     # In-memory storage engine logic

   ⚡ SUPPORTED COMMANDS:
   Command        Syntax         Description
PING          PING [message]    Returns PONG or echoes back the optional message string.
SET           SET key value     Stores a key-value pair in memory.
GET           GET key           Retrieves the value associated with a given key.
EXISTS        EXISTS key        Checks if a key exists in the database (1 if true, 0 if false).
DEL           DEL key           Deletes a key-value pair from storage.


  🚀GETTING STARTED:

  Prerequisites:

  1.Python 3.8+
  2. redis-cli (optional, for testing from the terminal)

  Running the Server:

  1. Clone or open the project directory in your terminal.

  2. Start the custom Redis server on port 6380 (to avoid conflicts with standard Redis instances):

            python server.py



Connecting with redis-cli
Open a second terminal window and connect to your custom server using the port flag:


            redis-cli -p 6380