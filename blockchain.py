import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

class Blockchain():

	def __init__(self):
		self.chain = []
		self.current_transaction = []
		#CREATES GENESIS BLOCK
		self.new_block(proof = 100, previous_hash = 1)
	
	def new_block(self, proof, previous_hash = None):
		
		#CREATES A NEW BLOCK AND ADDS IT TO CHAIN
		block = {
		'index': len(self.chain) + 1,
		'timestamp': time(),
		'transactions': self.current_transaction,
		'proof': proof,
		'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}

		#UPDATE CURRENT TRANSACTION
		self.current_transaction = []

		#ADD NEW BLOCK TO CHAIN
		self.chain.append(block)

		return block
		

	def new_transaction(self, sender, reciever, amount):
		#ADDS A NEW TRANSACTION TO LIST OF TRANSACTIONS
		self.current_transaction.append( {
			'sender': sender,
			'reciever': reciever,
			'amount':amount
			}
			)
		return self.last_block['index'] + 1
		
		

	@staticmethod
	def hash():
		#HASHES THE BLOCKS
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

		

	@property
	def last_block():
		#RETURNS THE BLOCK TO CHAIN
		return self.chain[-1]

###############################################################	PROOF OF WORK ########################################################

def proof_of_work():

	proof = 0

	while self.valid_proof is False:
		proof += 1
		return proof

def valid_proof(last_proof, proof):
	guess = '{last_proof}{proof}'.encode()
	guess_hash = hashlib.sha256(guess).hexdigest()
	return guess_hash[:4] == "0000"

############################################################## BLOCKCHAIN API #######################################################

app = Flask(__name__)
 
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods = ['POST'])
def new_transaction():
	values = request.get_json()

	##check all fields are filled
	required = ['sender', 'reciever', 'amount']
	if not all(k in values for k in required):
		return 'missing values', 400

	index = blockchain.new_transaction(values['sender'], values['reciever'], values['amount'])
	response = {'message': 'Transaction will be added to block {index}'}
	return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
	response = {
	'chain': blockchain.chain,
	'length': len(blockchain.chain)
	}

	return jsonify(response), 200

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000)

