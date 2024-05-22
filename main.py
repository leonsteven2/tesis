from flet import (Page,
    app,
    UserControl,
    Container,
    BoxShadow,
    ShadowBlurStyle,
    border,
    Row,
    Animation,
    alignment,
    Stack,
    ClipBehavior,
    TextButton,
    Column,
    AppView

)
import constants
from math import pi

class RobotExpressions(UserControl):
    def __init__(self, base_color):
        super().__init__()
        self.base_color = constants.neutral_color

        # Medidas de ojos, boca y cejas
        factor = 1
        self.eye_width = 150*factor
        self.eye_height = 150*factor
        self.mouth_width = 110*factor
        self.mouth_height = 110*factor
        self.eyebrow_width = 80*factor
        self.eyebrow_height = 15*factor

        self.padding = 20

        self.is_animation_finished = False
        # Creamos el ojo izquierdo
        self.left_eye_aux = self.eye_aux(eye_width=self.eye_width, eye_height=self.eye_height, radio_borde=self.eye_width)
        self.left_cont_aux = self.cont_aux(eye_width=self.eye_width, eye_height=self.eye_height)
        self.left_eye = self.create_eye(
            eye_width=self.eye_width,
            eye_height=self.eye_height,
            eye_aux=self.left_eye_aux,
            cont_aux=self.left_cont_aux,
        )

        # Creamos el ojo derecho
        self.right_eye_aux = self.eye_aux(eye_width=self.eye_width, eye_height=self.eye_height, radio_borde=self.eye_width)
        self.right_cont_aux = self.cont_aux(eye_width=self.eye_width, eye_height=self.eye_height)

        self.right_eye = self.create_eye(
            eye_width=self.eye_width,
            eye_height=self.eye_height,
            eye_aux=self.right_eye_aux,
            cont_aux=self.right_cont_aux,
        )

        # Creamos la boca
        self.mouth_aux = self.eye_aux(eye_height=self.mouth_height, eye_width=self.mouth_width, radio_borde=self.mouth_width)
        self.mouth_aux.opacity = 0
        self.mouth_cont = self.cont_aux(eye_width=self.mouth_width, eye_height=self.mouth_height)
        self.mouth = self.create_eye(
            eye_width=self.mouth_width,
            eye_height=self.mouth_height,
            eye_aux=self.mouth_aux,
            cont_aux=self.mouth_cont,
            function=self.test_function
        )

        # Creamos las cejas
        self.right_eyebrow = self.eye_aux(eye_height=self.eyebrow_height, eye_width=self.eyebrow_width, radio_borde=self.eyebrow_height)
        self.left_eyebrow = self.eye_aux(eye_height=self.eyebrow_height, eye_width=self.eyebrow_width, radio_borde=self.eyebrow_height)


        # Creamos fila de botones para generar expresiones
        self.btn_expressions = Row(
            alignment="center",
            controls=[
                TextButton(
                    "Alegría",
                    on_click=self.happy_animation
                ),
                TextButton(
                    "Tristeza",
                    on_click=self.sad_animation
                ),
                TextButton(
                    "Sorpresa",
                    on_click=self.surprised_animation
                ),
                TextButton(
                    "Enojo",
                    on_click=self.angry_animation
                ),
                TextButton(
                    "Neutral",
                    on_click=self.neutral_animation
                )
            ]
        )

        # Creamos el stack que contiene ojos y boca
        altura = self.eye_height+self.mouth_height+self.eyebrow_height+self.padding
        width = 2*self.eye_width+5*self.padding
        self.altura = altura
        self.width = width
        self.mouth.bottom = 0
        self.mouth.left = width/2 - self.mouth_width/1.75

        self.left_eye.top = 0

        self.right_eye.right = 0
        self.right_eye.top=0

        self.distancia_ceja_izquierda = self.eyebrow_width / 2
        self.left_eyebrow.left = self.distancia_ceja_izquierda
        self.left_eyebrow.top = -30

        self.distancia_ceja_derecha = width/2 + self.eyebrow_width
        self.right_eyebrow.left = self.distancia_ceja_derecha
        self.right_eyebrow.top = -30

        self.stack_main = Container(
            bgcolor="black",
            content=Stack(
                width=width,
                height=altura,
                clip_behavior=ClipBehavior.NONE,
                controls=[
                    self.mouth,
                    self.left_eye,
                    self.right_eye,
                    self.left_eyebrow,
                    self.right_eyebrow,

                ]
            )
        )

        self.col_main = Column(
            horizontal_alignment="center",
            controls=[
                self.stack_main,
                self.btn_expressions
            ]
        )

    def build(self):

        return self.col_main


    def create_eye(self, eye_width, eye_height, eye_aux, cont_aux, function=None):
        return Container(
            bgcolor="black",
            width=eye_width+self.padding,
            height=eye_height+self.padding,
            clip_behavior=ClipBehavior.NONE,
            alignment=alignment.center,
            animate_position=Animation(1000, "easeInOut"),
            on_animation_end=function,
            border_radius=eye_width/2,
            content=Stack(
                width=eye_width+self.padding,
                height=eye_height+self.padding,
                controls=[
                    eye_aux,
                    cont_aux
                ],
            )
        )

    def eye_aux(self, eye_width, eye_height, borde=False, radio_borde=None):
        cont = Container(
            width=eye_width,
            height=eye_height,
            bgcolor=self.base_color,
            border_radius=radio_borde,
            clip_behavior=ClipBehavior.NONE,
            #animate_size=Animation(1000, "easeIn"),
            animate_opacity=Animation(250, "easeInOut"),
            animate_position=Animation(750, "easeInOut"),
            animate_scale=Animation(750, "easeInOut"),
            animate_rotation=Animation(750, "easeInOut"),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=10,
                color=self.base_color,
                blur_style=ShadowBlurStyle.OUTER
            ),
            left=self.padding/2,
            top=self.padding/2
        )
        if borde == True:
            cont.border = border.all(1, "white")
        return cont

    def cont_aux(self, eye_width, eye_height, borde=False):
        cont = Container(
            width=eye_width,
            height=eye_height,
            bgcolor="black",
            border_radius=eye_width,
            animate_position=Animation(750, "easeInOut"),
            animate_scale=Animation(750, "easeInOut"),
            clip_behavior=ClipBehavior.NONE,
            #animate_opacity=Animation(500, "easeInOut"),
            shadow=BoxShadow(
                spread_radius=0,
                blur_radius=15,
                color="black",
                blur_style=ShadowBlurStyle.OUTER
            ),
            top=eye_height*1.1,
            left=self.padding/2
        )

        if borde == True:
            cont.border = border.all(5, "white")

        return cont

    def happy_animation(self, ctrl):
        # Animaciones internas ---------------------------
        self.left_cont_aux.top = self.eye_height / 1.75
        self.left_cont_aux.left = self.padding / 2
        self.left_cont_aux.scale = 1

        self.right_cont_aux.top = self.eye_height / 1.75
        self.right_cont_aux.left = self.padding / 2
        self.right_cont_aux.scale = 1

        self.change_color_eye(constants.happy_color)

        # Animaciones de boca
        self.mouth_aux.width = self.mouth_width
        self.mouth_aux.right = self.padding / 2
        self.mouth_aux.height = self.mouth_height

        self.mouth_aux.opacity = 1
        self.mouth_cont.opacity = 1
        self.mouth_cont.top = -self.mouth_height/2.5
        self.mouth_cont.left = self.padding/2
        self.mouth_cont.scale = 1.5

        # Animaciones de cejas
        self.left_eyebrow.left = self.distancia_ceja_izquierda - self.padding
        self.left_eyebrow.top = -25
        self.left_eyebrow.rotate = -0.2

        self.right_eyebrow.left = self.distancia_ceja_derecha + self.padding
        self.right_eyebrow.top = -25
        self.right_eyebrow.rotate = 0.2

        # Animaciones externas ---------------------------
        self.mouth.bottom = self.mouth_height/2
        self.mouth_aux.scale = 1




        self.col_main.update()

    def sad_animation(self, ctrl):
        self.left_cont_aux.top = -self.eye_height / 1.75
        self.left_cont_aux.left = self.padding/2
        self.left_cont_aux.scale = 1.5

        self.right_cont_aux.top = -self.eye_height / 1.75
        self.right_cont_aux.left = self.padding/2
        self.right_cont_aux.scale = 1.5

        self.change_color_eye(constants.sad_color)

        # Animaciones de boca
        self.mouth_aux.width = self.mouth_width
        self.mouth_aux.right = self.padding / 2
        self.mouth_aux.height = self.mouth_height

        self.mouth_aux.opacity = 1
        self.mouth_cont.opacity = 1
        self.mouth_cont.top = self.mouth_height / 1.75
        self.mouth_cont.left = self.padding / 2
        self.mouth_cont.scale = 1.3

        # Animaciones de cejas
        self.left_eyebrow.left = self.distancia_ceja_izquierda
        self.left_eyebrow.top = self.padding
        self.left_eyebrow.rotate = -0.5

        self.right_eyebrow.left = self.distancia_ceja_derecha
        self.right_eyebrow.top = self.padding
        self.right_eyebrow.rotate = 0.5

        # Animaciones externas ---------------------------
        self.mouth.bottom = 0
        self.mouth_aux.scale = 1

        self.col_main.update()

    def surprised_animation(self, ctrl):
        self.left_cont_aux.top = 0
        self.left_cont_aux.left = self.padding / 2
        self.left_cont_aux.scale = 0.25

        self.right_cont_aux.top = 0
        self.right_cont_aux.left = self.padding / 2
        self.right_cont_aux.scale = 0.25

        self.change_color_eye(constants.surprised_color)

        # Animaciones de boca
        self.mouth_aux.width = self.mouth_width
        self.mouth_aux.right = self.padding / 2
        self.mouth_aux.height = self.mouth_height

        self.mouth_aux.opacity = 1
        self.mouth_aux.scale = 0.6
        self.mouth_cont.scale = 1
        self.mouth_cont.top = self.mouth_height*1.3

        # Animaciones de cejas
        self.left_eyebrow.left = self.distancia_ceja_izquierda
        self.left_eyebrow.top = -30
        self.left_eyebrow.rotate = 0

        self.right_eyebrow.left = self.distancia_ceja_derecha
        self.right_eyebrow.top = -30
        self.right_eyebrow.rotate = 0

        # Animaciones externas ---------------------------
        self.mouth.bottom = self.mouth_height/5


        self.col_main.update()

    def neutral_animation(self, ctrl):
        # Animaciones de ojo izquierdo
        self.left_cont_aux.top = self.eye_height * 1.1
        self.left_cont_aux.left = self.padding / 2
        self.left_cont_aux.scale = 1

        # Animaciones de ojo derecho
        self.right_cont_aux.top = self.eye_height * 1.1
        self.right_cont_aux.left = self.padding / 2
        self.right_cont_aux.scale = 1

        self.change_color_eye(constants.neutral_color)

        # Animaciones de boca
        self.mouth_aux.opacity = 0.75
        self.mouth_aux.scale = 1

        self.mouth_aux.width = 2*self.mouth_width
        self.mouth_aux.right = self.padding/2
        self.mouth_aux.height = self.mouth_height*0.3

        self.mouth_cont.top = self.mouth_height*1.3

        # Animaciones de cejas
        self.left_eyebrow.opacity = 0.75
        self.left_eyebrow.left = self.distancia_ceja_izquierda
        self.left_eyebrow.top = -30
        self.left_eyebrow.rotate = 0

        self.right_eyebrow.opacity = 0.75
        self.right_eyebrow.left = self.distancia_ceja_derecha
        self.right_eyebrow.top = -30
        self.right_eyebrow.rotate = 0

        # Animaciones externas ---------------------------
        self.mouth.bottom = -self.padding


        self.col_main.update()

    def angry_animation(self, ctrl):
        self.left_cont_aux.top = -self.eye_height / 1.25
        self.left_cont_aux.left = self.eye_height / 2.5
        self.left_cont_aux.scale = 2

        self.right_cont_aux.top = -self.eye_height / 1.25
        self.right_cont_aux.left = -self.eye_height / 2.5 + self.padding
        self.right_cont_aux.scale = 2

        self.change_color_eye(constants.angry_color)

        # Animaciones de boca
        self.mouth_aux.width = self.mouth_width
        self.mouth_aux.right = self.padding / 2
        self.mouth_aux.height = self.mouth_height

        self.mouth_aux.opacity = 1
        self.mouth_aux.scale = 1
        self.mouth_cont.opacity = 1
        self.mouth_cont.top = self.mouth_height / 1.75
        self.mouth_cont.left = self.padding / 2
        self.mouth_cont.scale = 1.5



        # Animaciones de cejas
        self.left_eyebrow.left = self.distancia_ceja_izquierda + 3*self.padding
        self.left_eyebrow.top = 30
        self.left_eyebrow.rotate = 0.75

        self.right_eyebrow.left = self.distancia_ceja_derecha - 3*self.padding
        self.right_eyebrow.top = 30
        self.right_eyebrow.rotate = -0.75

        # Animaciones externas ---------------------------
        self.mouth.bottom = -1

        self.col_main.update()

    def change_color_eye(self, color):
        self.left_eye_aux.bgcolor = color
        self.left_eye_aux.shadow.color = color

        self.right_eye_aux.bgcolor = color
        self.right_eye_aux.shadow.color = color

        self.mouth_aux.bgcolor = color
        self.mouth_aux.shadow.color = color

        self.left_eyebrow.bgcolor = color
        self.left_eyebrow.shadow.color = color
        self.right_eyebrow.bgcolor = color
        self.right_eyebrow.shadow.color = color

    def test_function(self, e):
        print("anima")
        padding = 5
        if self.is_animation_finished == False:
            self.right_eye.top = - padding
            self.left_eye.top = - padding
            self.left_eyebrow.top = int(self.left_eyebrow.top) - padding
            self.right_eyebrow.top = int(self.right_eyebrow.top) - padding
            self.mouth.bottom = int(self.mouth.bottom) - padding
            self.is_animation_finished = True
            self.col_main.update()
        else:
            self.right_eye.top = padding
            self.left_eye.top = padding
            self.left_eyebrow.top = int(self.left_eyebrow.top) + padding
            self.right_eyebrow.top = int(self.right_eyebrow.top) + padding
            self.mouth.bottom = int(self.mouth.bottom) + padding
            self.is_animation_finished = False
            self.col_main.update()




def main(page: Page):
    page.title = "Tesis"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "black"

    robot = RobotExpressions(base_color="green")

    page.add(
        robot
    )

if __name__ == "__main__":
    app(target=main, view=AppView.WEB_BROWSER)

