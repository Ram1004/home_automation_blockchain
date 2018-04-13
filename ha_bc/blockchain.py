from block import Block
import datetime
import json
def add_newblock(chain,data):
    return Block(chain[-1].hash,data,datetime.datetime.now())

chain = [Block.create_genesis_block()]
chain.append(add_newblock(chain,4))
chain.append(add_newblock(chain,3))
chain.append(add_newblock(chain,5))
d = chain
