import sqlite3
import random 
clientes = [
{ 'id': 1, 'rut': '18620855-1', 'name': 'Angel Serrano' },
{ 'id': 2, 'rut': '11345435-2', 'name': 'Roser Abreu' },
{ 'id': 3, 'rut': '14256777-k', 'name': 'Rosa Campos' },
{ 'id': 4, 'rut': '12675688-0', 'name': 'Celestino Fuentes' },
{ 'id': 5, 'rut': '14234334-4', 'name': 'Rebeca Rojas' },
{ 'id': 6, 'rut': '10152323-8', 'name': 'Andrea Palomo' },
{ 'id': 7, 'rut': '15587715-4', 'name': 'Maria Inmaculada Jiménez' },
{ 'id': 8, 'rut': '15034590-7', 'name': 'Marcela Navarro' },
{ 'id': 9, 'rut': '11804345-3', 'name': 'Francisco Manuel Gago' },
{ 'id': 10, 'rut': '13804238-0', 'name': 'Patricio Duran' }, ]

# Registro de Empresas dedicadas el rubro de arriendo de autos:
empresas = [
{ 'id': 1, 'name': 'CHILE ARRIENDA AUTOS S.A' }, { 'id': 2, 'name': 'AUTOK S.A' },
{ 'id': 3, 'name': 'RENT A CAR S.A' },
]
# Registro de arriendo de autos en un mes:
arriendos = [
{ 'id_cliente': 6, 'id_empresa': 1, 'costo_diario': 15000, 'dias': 3}, 
{ 'id_cliente': 1, 'id_empresa': 3, 'costo_diario': 18000, 'dias': 2}, 
{ 'id_cliente': 5, 'id_empresa': 3, 'costo_diario': 135000, 'dias': 1},
{ 'id_cliente': 2, 'id_empresa': 2, 'costo_diario': 5600, 'dias': 4},
{ 'id_cliente': 3, 'id_empresa': 1, 'costo_diario': 23000, 'dias': 3},
{ 'id_cliente': 7, 'id_empresa': 2, 'costo_diario': 15000, 'dias': 3},
{ 'id_cliente': 8, 'id_empresa': 3, 'costo_diario': 45900, 'dias': 2},
{ 'id_cliente': 10, 'id_empresa': 3, 'costo_diario': 19000, 'dias': 5},
{ 'id_cliente': 9, 'id_empresa': 3, 'costo_diario': 51000, 'dias': 7},
{ 'id_cliente': 5, 'id_empresa': 1, 'costo_diario': 89000, 'dias': 7},
{ 'id_cliente': 1, 'id_empresa': 2, 'costo_diario': 16000, 'dias': 1},
{ 'id_cliente': 3, 'id_empresa': 3, 'costo_diario': 37500, 'dias': 1},
{ 'id_cliente': 6, 'id_empresa': 1, 'costo_diario': 19200, 'dias': 2},
{ 'id_cliente': 6, 'id_empresa': 3, 'costo_diario': 10000, 'dias': 3},
{ 'id_cliente': 6, 'id_empresa': 2, 'costo_diario': 5900, 'dias': 2},
{ 'id_cliente': 10, 'id_empresa': 1, 'costo_diario': 9000, 'dias': 5},
{ 'id_cliente': 10, 'id_empresa': 3, 'costo_diario': 13500, 'dias': 5},
{ 'id_cliente': 9, 'id_empresa': 1, 'costo_diario': 38200, 'dias': 4},
{ 'id_cliente': 7, 'id_empresa': 2, 'costo_diario': 17000, 'dias': 1},
{ 'id_cliente': 5, 'id_empresa': 3, 'costo_diario': 1000, 'dias': 10},
{ 'id_cliente': 1, 'id_empresa': 2, 'costo_diario': 6000, 'dias': 20},
{ 'id_cliente': 3, 'id_empresa': 1, 'costo_diario': 16200, 'dias': 7},
{ 'id_cliente': 2, 'id_empresa': 2, 'costo_diario': 10000, 'dias': 5} ]


def insert_data():
    db = sqlite3.connect('db.sqlite3')
    cur = db.cursor()

    # cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    cur.execute("SELECT * FROM arriendos_arriendos")
    colnames = cur.description
    # print(cur.fetchall())
    print(colnames)

    for i in empresas:
        print("empresas")
        print(i)
        cur.execute('INSERT INTO empresa_empresa (id, name) VALUES(:id, :name);', i)
        db.commit()

    for clte in clientes:
        print('clientes')
        nombres=(clte['name']).split()
        if len(nombres[:-1])==2: 
            clte['name']=nombres[:-1][0]+' '+ nombres[:-1][1]
        else: 
            clte['name']=nombres[:-1][0]
        clte['lastname']=nombres[-1]
        cur.execute('INSERT INTO cliente_cliente(id, rut,name, lastname) VALUES(:id, :rut, :name, :lastname);', clte)
        db.commit()

    for arr in arriendos:
        print("arriendos")
        print(arr)
        arr['cliente_id']=arr.pop('id_cliente')
        arr['empresa_id']=arr.pop('id_empresa')
        arr['fecha_arriendo']='2022-'+str(random.randint(1,12)).zfill(2)+'-'+str(random.randint(1,30)).zfill(2)
        
        print("2): ",arr)
        cur.execute('INSERT INTO arriendos_arriendos (costo_diario, dias, fecha_arriendo, cliente_id, empresa_id) VALUES(:costo_diario, :dias,:fecha_arriendo, :cliente_id, :empresa_id);', arr)
        db.commit()
if __name__ == "__main__":
    insert_data()