import myconnutils

connection = myconnutils.getConnectionEkudemic()
cursor = connection.cursor()

query = "SELECT * FROM public.estudiante_foto"
# query = "SELECT *  FROM information_schema.columns WHERE table_schema = 'public' AND table_name   = 'estudiante_foto' "

cursor.execute(query)
records = cursor.fetchall()


nombres = []
tipo = []

columns_sp = []

colums_update = []

str2 = " " 


for record in records:
    open("h:/fotos/"+record[2]+'.jpeg', 'wb') .write(record[3])
    # print(record)
    # nombres.append(record[3])
    # tipo.append(record[7])
    # # columns_sp.append("DECLARE v"+ str(record[3]).capitalize()+' '+ record['data_type'] + ';\n')
    # columns_sp.append("SET v"+ str(record[3]).capitalize()+"=  JSON_EXTRACT(pParametroJson, CONCAT('$[', vIndex, ']."+str(record[3])+"'));\n")
    # colums_update.append(" "+ str(record[3])+" = v"+ str(record[3]).capitalize()+",\n")
    
    

print(nombres)
print(tipo)
print(str2.join(colums_update))
connection.close()

