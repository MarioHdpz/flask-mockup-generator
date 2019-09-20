
# Mockup Generator con Flask

Lo prometido es deuda, aquí está lo que vimos de Flask en el taller de Bedu.

Clónenlo, jueguen con él, rómpanlo si quieren.

Si tienen dudas no duden en contactarme, gracias por asistir hoy.

Happy coding!

### Instrucciones para correrlo

1. Instalar pipenv 

    `pip install pipenv`

2. Instalar dependencias (Ya vienen especificadas en el Pipfile)

    `pipenv install`

3. Entren a su ambiente virtual

    `pipenv shell`

4. Corran el server de Flask

    `flask run`

Recuerden que pueden consumirlo desde cualquier REST API Client, la peticion debe ser un POST con contenido JSON que tenga la siguiente estructura:

```
{
	"title": "Bedu Flask Workshop",
	"premiere_date": "19/09/19",
	"cast": [
		"Fullstack Pythons",
		"Mario HD"
	]
}
```
