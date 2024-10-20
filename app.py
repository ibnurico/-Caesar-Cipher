from flask import Flask, render_template, request, jsonify
import string

app = Flask(__name__)

# Fungsi untuk melakukan Caesar cipher dan menggeser huruf
def caesar_cipher(text, shift):
    result = []
    for char in text.upper():
        if char in string.ascii_uppercase:
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

# Fungsi untuk menghitung frekuensi huruf dalam teks
def calculate_frequencies(text):
    text = text.upper()  # Mengubah teks menjadi huruf kapital
    letter_counts = {char: 0 for char in string.ascii_uppercase}
    
    for char in text:
        if char in letter_counts:
            letter_counts[char] += 1
            
    return [letter_counts[char] for char in string.ascii_uppercase]

# Fungsi frekuensi standar bahasa Inggris
def standard_english_frequencies():
    return [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.09, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.15, 2.0, 0.07]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text", "")
        shift = int(request.form.get("shift", 0))
        
        # Enkripsi/shift alfabet dan hitung frekuensi
        shifted_text = caesar_cipher(text, shift)
        shifted_alphabet = caesar_cipher(string.ascii_uppercase, shift)
        original_frequencies = calculate_frequencies(text)
        standard_frequencies = standard_english_frequencies()
        
        return jsonify({
            "original_frequencies": original_frequencies,
            "standard_frequencies": standard_frequencies,
            "shifted_alphabet": shifted_alphabet,
            "output_text": shifted_text
        })
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
