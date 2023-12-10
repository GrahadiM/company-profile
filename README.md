### Step by step membuat Web dengan FLASK PYTHON
- Tuliskan command menggunakan terminal : <code>pip install Flask</code>
- Buat file dengan nama app.py, lalu masukan code dibawah :
<code>from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)</code>
- Buat folder dengan nama ```templates``` untuk membuat folder Frontend.
- Buat file dengan nama ```index.html``` untuk membuat file HTML yang akan digunakan sebagai root utama.
- Buat folder dengan nama ```assets``` untuk membuat folder semua asset (css, js, gambar, dll).

### Struktur Folder dan file
<code>- your_project_folder
  - templates
    - index.html
  - assets
    - css
      - styles.css
    - js
      - app.js
    - images
      - your_image.jpg</code>

### Run Server
- Tuliskan command menggunakan terminal:
<code>python app.py</code>

### Notes
- [x] Program ini untuk pembelajaran basic.
- [ ] Program ini untuk pembelajaran expert.
- [x] Program ini menggunakan server local.
- [ ] Program ini menggunakan server public.