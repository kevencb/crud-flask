from flask import Flask, render_template, jsonify, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "flask_store"

cellphones = [
    {"id": 1, "brand": "Apple", "model": "iPhone 13", "price": 799},
    {"id": 2, "brand": "Samsung", "model": "Galaxy S22", "price": 699},
    {"id": 3, "brand": "Google", "model": "Pixel 7", "price": 599},
]

customers = [
{   "id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

suppliers = [
    {"id": 1, "name": "Tech Supplies Co.", "contact": "contact@techsupplies.com"},
    {"id": 2, "name": "Gadget World", "contact": "info@gadgetworld.com"},
    {"id": 3, "name": "Mobile Hub", "contact": "support@mobilehub.com"},
]

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/customers')
# def list_customers():
#     return render_template("customers.html", customers = customers)

# @app.route('/cellphones')
# def list_cellphones():
#     return render_template("cellphones.html", cellphones = cellphones)

# @app.route('/suppliers')
# def list_suppliers():
#     return render_template("suppliers.html", suppliers = suppliers)

# #**** FORMULARIO ******
# @app.post('/')
# def create_cellphone():
#     global cellphones
#     new_id = len(cellphones) + 1
#     new_cellphone = {
#         "id": new_id,
#         "brand": request.form["brand"],
#         "model": request.form["model"],
#         "price": float(request.form["price"]),
#     }
#     cellphones.append(new_cellphone)
#     flash("Celular agregado correctamente 🎉")
#     return redirect(url_for("get_cellphones"))

#**** CRUD CELLPHONES ******
#Cargar todos los celulares
@app.route('/cellphones', methods=['GET'])
def get_cellphones():
    return jsonify(cellphones)

#Cargar un celular por ID
@app.route('/cellphones/<int:id>', methods=["GET"])
def get_cellphone(id):
    cellphone = next((c for c in cellphones if c["id"] == id), None)
    if cellphone:
        return jsonify(cellphone)
    return jsonify({"error": "Cellphone not found"}), 404

#Agregar un nuevo celular
@app.route('/cellphones', methods=['POST'])
def add_cellphone():
    new_cellphone = request.json
    cellphones.append(new_cellphone)
    return jsonify(new_cellphone), 201

#Editar un celular existente
@app.route('/cellphones/<int:id>', methods=['PUT'])
def update_cellphone(id):
    cellphone = next((c for c in cellphones if c["id"] == id), None)
    if cellphone:
        data = request.json
        cellphone.update(data)
        return jsonify(cellphone)
    return jsonify({"error": "Cellphone not found"}), 404

#Eliminar un celular
@app.route('/cellphones/<int:id>', methods=['DELETE'])
def delete_cellphone(id):
    for cellphone in cellphones:
        if cellphone["id"] == id:
            cellphones.remove(cellphone)
            return jsonify({"message": "Cellphone deleted"})
    return jsonify({"error": "Cellphone not found"}), 404


#**** CRUD CUSTOMERS ******
#Cargar todos los clientes
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

#Cargar un cliente por ID
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = next((c for c in customers if c["id"] == id), None)
    if customer:
        return jsonify(customer)
    return jsonify({"error": "Customer not found"}), 404

#Agregar un nuevo cliente
@app.route('/customers', methods=['POST'])
def add_customer():
    new_customer = request.json
    customers.append(new_customer)
    return jsonify(new_customer), 201

#Editar un cliente
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = next((c for c in customers if c["id"] == id), None)
    if customer:
        data = request.json
        customer.update(data)
        return jsonify(customer)
    return jsonify({"error": "Customer not found"}), 404

#Eliminar un cliente
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = next((c for c in customers if c["id"] == id), None)
    if customer:
        customers.remove(customer)
        return jsonify({"message": "Customer removed"}), 200
    return jsonify({"error": "Customer not found"}), 404


#**** CRUD SUPPLIERS ******
#Cargar todos los proveedores
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    return jsonify(suppliers)

#Crear un proveedor
@app.route('/suppliers', methods=['POST'])
def add_supplier():
    new_supplier = request.json
    suppliers.append(new_supplier)
    return jsonify(new_supplier), 201

#Cargar un proveedor por ID
@app.route('/suppliers/<int:id>', methods=['GET'])
def supplier(id):
    supplier = next((s for s in suppliers if s["id"] == id), None)
    if supplier:
        return jsonify(supplier)
    return jsonify({"error": "Supplier not found"})

#Editar un proveedor
@app.route('/suppliers/<int:id>', methods=['PUT'])
def update_supplier(id):
    supplier = next((s for s in suppliers if s["id"] == id), None)
    if supplier:
        data = request.json
        supplier.update(data)
        return jsonify(supplier), 201
    return jsonify({"error": "Supplier not found"}), 404

#Eliminar un proveedor
@app.route('/suppliers/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    supplier = next((s for s in suppliers if s["id"] == id), None)
    if supplier:
        suppliers.remove(supplier)
        return jsonify({"message": "Supplier removed"}), 200
    return jsonify({"error": "Supplier not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)