# Pokemon_Table
Lo que se realizó es un script usando Python y sus librerías Pandas y SQLalchemy y MySQL como gestor de base de datos.


# Funcionamiento y Como se pensó
Lo que hace el script es que lee un archivo CSV y crea tablas en una base de datos que se dividen por el Type 1.
Los problemas que se presentaron fueron que al momento de cargar los pokemones no se llegaban a crear las tablas de ese tipo y eso llevaba a un error, entonces lo que se realizó para solucionarlos es que usando
pandas se agrupen por tipos y esto permitió que a medida que se creen las tablas inserten todos los pokemones de ese tipo.
