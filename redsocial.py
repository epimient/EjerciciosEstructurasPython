#Perfil de red social
perfil = {
    "nombre": "Ricardo",
    "ciudad": "Barranquilla",
    "edad": 20,
    "amigos":[
        { "nombre":"Pepito", "tiempo_amistad": 5},
        { "nombre":"Juan", "tiempo_amistad": 2}, 
        { "nombre":"Alberto", "tiempo_amistad": 10} 
        ],
    "posts":[
        {"contenido": "me gusta el cafe", 
         "likes":2,
         "comentarios":[
             {"usuario": "Pepito", "texto": "no me gusta el café a mi"}
         ]}
             ]
}

#agregar un nuevo post
nuevo_post ={
    "contenido": "Alberto, me la suda",
    "likes": 3,
    "comentarios": [{"usuario": "Pepito", "texto": "me gusta"}]}

perfil["posts"].append(nuevo_post)

#modificar la ciudad
perfil["ciudad"] = "Madrid"

# eliminar segundo amigo
del perfil["amigos"][1]

#imprimir el perfil
print("perfil:")
print(f"nombre: {perfil['nombre']} \nciudad: {perfil['ciudad']} \nedad: {perfil['edad']}")
print("amigos:")
for amigo in perfil["amigos"]:
    print(f"nombre: {amigo['nombre']} \ntiempo de amistad: {amigo['tiempo_amistad']}")

print("posts:")
for post in perfil["posts"]:
    print(f"contenido: {post['contenido']}")
    print(f"likes: {post['likes']}")
    if post["comentarios"]:
        print("comentarios:")
        for comentario in post["comentarios"]:
            print(f"usuario: {comentario['usuario']}")
            print(f"texto: {comentario['texto']}")
    else:
        print("no hay comentarios")


    
