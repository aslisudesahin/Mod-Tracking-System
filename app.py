from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- DATA (English) ---
# We changed keys: ad->name, kategori->developer, surum->version, aciklama->description, durum->status
mods_list = [
    {
        "id": 1,
        "name": "SkyUI", 
        "developer": "SkyUI Team", 
        "version": "5.2", 
        "description": "Elegant, PC-friendly UI mod for Skyrim with many advanced features.",
        "status": "Active"
    },
    {
        "id": 2,
        "name": "Realistic Water Two", 
        "developer": "Isoku", 
        "version": "1.1", 
        "description": "One of the most popular water modification mods that makes water realistic.",
        "status": "Active"
    }
]

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html', mods=mods_list)

@app.route('/mod/<int:id>')
def mod_detail(id):
    # Find mod by ID
    selected_mod = next((mod for mod in mods_list if mod['id'] == id), None)
    if selected_mod is None:
        return "Mod not found", 404
    return render_template('detay.html', mod=selected_mod)

@app.route('/add-mod', methods=['GET', 'POST'])
def add_mod():
    if request.method == 'POST':
        # Auto-increment ID
        new_id = 1 if not mods_list else mods_list[-1]['id'] + 1
        
        # Get English form data
        name = request.form.get('name')
        developer = request.form.get('developer')
        version = request.form.get('version')
        description = request.form.get('description')
        
        # Checkbox logic
        status_check = request.form.get('status')
        status = "Active" if status_check else "Inactive"

        # Append to list
        mods_list.append({
            "id": new_id,
            "name": name,
            "developer": developer,
            "version": version,
            "description": description,
            "status": status
        })
        
        return redirect(url_for('home'))
    
    return render_template('mod_ekle.html')

@app.route('/delete/<int:id>')
def delete_mod(id):
    global mods_list
    # Filter out the mod with the matching ID
    mods_list = [mod for mod in mods_list if mod['id'] != id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)