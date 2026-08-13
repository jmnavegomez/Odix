# Composición

## Introducción

La composición es un mecanismo mediante el cual una clase utiliza objetos de otras clases para construir su comportamiento. 

Contrasta con la herencia en que al heredar las clases hijas ganan todos los atributos y métodos de la clase padre aunque luego puedan sobreescribirlos. En la composición la clase no hereda los atributos ni los métodos de las clases que la forman, sino que puede utilizarlos a través de los objetos que contiene. La herencia modela una relación de especialización ("es un"), mientras que la composición modela una relación de agregación ("tiene un").

Se suele preferir la composición frente a la herencia a la hora de programar porque tiene un menor acoplamiento y ofrece una mayor flexibilidad. De ahí la conocida recomendación: ·"Favor composition over inheritance."·

## Uso de la composición

Para usar la composición basta con almacenar objetos de otras clases como atributos de una clase. Estos objetos pueden crearse internamente o recibirse como parámetros durante la inicialización.

Una vez que se tiene la instancia dentro de la clase, esta puede utilizar los métodos y atributos de los objetos que la componen.

## Ejemplo

En el siguiente ejemplo se ve cómo es una composición:

``` python
class EmailService:

    def enviar(self, mensaje):
        print(f"Email: {mensaje}")


class Persona:

    def __init__(self):
        self.email = EmailService()

    def avisar(self):
        self.email.enviar("Hola")
``` 

La clase `Persona` contiene un objeto de la clase `EmailService`, cuyo método `enviar()` utiliza para enviar un mensaje. 

Por lo tanto, `Persona` no hereda los métodos de `EmailService`, sino que los utiliza a través del objeto `email`. `Persona` delega la responsabilidad de enviar correos en `EmailService`.

## Conclusión

En POO la composición permite construir objetos complejos a partir de otros más simples, delegando responsabilidades entre ellos y favoreciendo un diseño más flexible y con menor acoplamiento que la herencia. Por ello, suele ser la opción preferida frente a la herencia cuando ambas permiten resolver el mismo problema.

::pagebreak
::