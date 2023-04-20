import os
from flask import Flask, request, jsonify
from datetime import datetime
import eratosthenes
import atkin
import sundaram

app = Flask(__name__)

ROOT_PATH = os.environ.get("ROOT_PATH", '')
UPPER_LIMIT = int(os.environ.get("UPPER_LIMIT", 1000000))
LOWER_LIMIT = int(os.environ.get("LOWER_LIMIT", 1))
DEFAULT_UPPER_LIMIT = int(os.environ.get("DEFAULT_UPPER_LIMIT", 100))

def handle_prime(find_primes):
    start_time = datetime.now()
    max_prime = int(request.args.get('limit', DEFAULT_UPPER_LIMIT))

    # Sanitize input
    if max_prime < LOWER_LIMIT or max_prime > UPPER_LIMIT:
        return f'Please submit a value from {LOWER_LIMIT} to {UPPER_LIMIT}', 400
    
    primes = find_primes(max_prime)
    
    return jsonify(microseconds = (datetime.now() - start_time).microseconds, primes = primes)

@app.route(f'{ROOT_PATH}/prime/eratosthenes', methods=['GET'])
def handle_eratosthenes():
    return handle_prime(eratosthenes.find_primes)

@app.route(f'{ROOT_PATH}/prime/sundaram', methods=['GET'])
def handle_sundaram():
    return handle_prime(sundaram.find_primes)

@app.route(f'{ROOT_PATH}/prime/atkin', methods=['GET'])
def handle_atkin():
    return handle_prime(atkin.find_primes)