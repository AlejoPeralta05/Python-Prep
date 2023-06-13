#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
list = ["Buenos Aires", "Paris", "Montecarlo", "Mendoza", "Junin"]
print(list)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(list[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(list[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(list))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:


print(list [2:])


# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:


print(list[:4])


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

list.append("Ciudad de Mexico")
# In[17]:

list.append("Montevideo")

# In[18]:

print(list)

# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

list.insert(3, "Quito")

# In[21]:

print(list)


# 9) Concatenar otra lista a la ya creada

# In[22]:

list.extend(["Cordoba", "San Luis", "Punta del este"])
print(list)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:


print(list.index("Montevideo"))


# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

print(list.index("Salta"))



# 12) Eliminar un elemento de la lista

# In[25]:

list.remove("Buenos Aires")
# In[26]:
print(list)

# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:





# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:





# 15) Mostrar la lista multiplicada por 4

# In[29]:




# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:




# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:




# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:





# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:





# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:





# 21) Convertir la tupla en una lista

# In[52]:





# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:





# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:






# 24) Imprimir las claves del diccionario

# In[59]:




# 25) Imprimir las ciudades a través de su clave

# In[61]:




