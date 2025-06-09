from cipher.railfence import RailFenceCipher
from flask import Flask, request, jsonify

app = Flask(__name__)
rail_fence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = rail_fence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({ 'encrypted_text': encrypted_text })

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = rail_fence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({ 'decrypted_text': decrypted_text })

if __name__ == '__main__':
    app.run()
