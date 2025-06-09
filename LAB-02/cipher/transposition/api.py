from cipher.transposition import TranspositionCipher
from flask import Flask, request, jsonify

app = Flask(__name__)
transposition_cipher = TranspositionCipher()

@app.route("/api/transposition/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    plain_text = data.get("plain_text")
    key = int(data.get("key"))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    cipher_text = data.get("cipher_text")
    key = int(data.get("key"))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == "__main__":
    app.run()
