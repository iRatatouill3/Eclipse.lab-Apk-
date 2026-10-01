from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen

KV = r"""
#:import dp kivy.metrics.dp

<NavButton@Button>:
    size_hint_y: None
    height: dp(46)
    background_normal: ""
    background_color: (0.10, 0.14, 0.26, 1)
    color: (1, 1, 1, 1)
    font_size: "15sp"

<Card@BoxLayout>:
    orientation: "vertical"
    padding: dp(16)
    spacing: dp(8)
    size_hint_y: None
    height: self.minimum_height
    canvas.before:
        Color:
            rgba: (0.07, 0.10, 0.19, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [18]

<TitleLabel@Label>:
    color: (1,1,1,1)
    font_size: "28sp"
    bold: True
    size_hint_y: None
    height: self.texture_size[1] + dp(8)
    text_size: self.width, None
    halign: "left"

<BodyLabel@Label>:
    color: (0.72, 0.77, 0.88, 1)
    font_size: "16sp"
    size_hint_y: None
    height: self.texture_size[1]
    text_size: self.width, None
    halign: "left"
    valign: "top"

ScreenManager:
    HomeScreen:
    TypesScreen:
    SimulatorScreen:
    SafetyScreen:
    QuizScreen:
    AboutScreen:

<HomeScreen>:
    name: "home"
    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: (0.02, 0.03, 0.08, 1)
            Rectangle:
                pos: self.pos
                size: self.size

        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(16)
                size_hint_y: None
                height: self.minimum_height

                Label:
                    text: "ECLIPSE LAB"
                    color: (1, 0.72, 0.02, 1)
                    font_size: "16sp"
                    bold: True
                    size_hint_y: None
                    height: dp(28)

                TitleLabel:
                    text: "Eclipses solares"

                BodyLabel:
                    text: "Aprende cómo la Luna puede ocultar al Sol, conoce los tipos de eclipse y prueba un simulador interactivo."

                Widget:
                    size_hint_y: None
                    height: dp(25)

                Label:
                    text: "☀"
                    font_size: "110sp"
                    color: (1, .65, .05, 1)
                    size_hint_y: None
                    height: dp(130)

                Label:
                    text: "●"
                    font_size: "95sp"
                    color: (.06, .07, .11, 1)
                    size_hint_y: None
                    height: dp(105)

                Card:
                    TitleLabel:
                        text: "¿Qué es un eclipse solar?"
                        font_size: "22sp"
                    BodyLabel:
                        text: "Ocurre cuando la Luna pasa entre el Sol y la Tierra y bloquea total o parcialmente la luz del Sol para algunas regiones del planeta."

                Card:
                    TitleLabel:
                        text: "Alineación"
                        font_size: "22sp"
                    BodyLabel:
                        text: "Sol  →  Luna  →  Tierra\\nLa Luna proyecta su sombra sobre una parte de la Tierra."

                Widget:
                    size_hint_y: None
                    height: dp(8)

        BoxLayout:
            size_hint_y: None
            height: dp(54)
            spacing: dp(4)
            padding: dp(4)
            NavButton:
                text: "Inicio"
                on_release: app.root.current = "home"
            NavButton:
                text: "Tipos"
                on_release: app.root.current = "types"
            NavButton:
                text: "Simular"
                on_release: app.root.current = "sim"
            NavButton:
                text: "Más"
                on_release: app.root.current = "about"

<TypesScreen>:
    name: "types"
    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: (0.02, 0.03, 0.08, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(14)
                size_hint_y: None
                height: self.minimum_height

                TitleLabel:
                    text: "Tipos de eclipse solar"

                Card:
                    TitleLabel:
                        text: "🌑 Eclipse total"
                        font_size: "22sp"
                    BodyLabel:
                        text: "La Luna cubre completamente el disco solar desde una zona específica de la Tierra."

                Card:
                    TitleLabel:
                        text: "🌘 Eclipse parcial"
                        font_size: "22sp"
                    BodyLabel:
                        text: "Solo una parte del Sol queda cubierta por la Luna."

                Card:
                    TitleLabel:
                        text: "⭕ Eclipse anular"
                        font_size: "22sp"
                    BodyLabel:
                        text: "La Luna se ve más pequeña que el Sol y deja visible un anillo brillante."

                Card:
                    TitleLabel:
                        text: "🌗 Eclipse híbrido"
                        font_size: "22sp"
                    BodyLabel:
                        text: "En distintos lugares de su trayectoria puede verse como total o anular."

        BoxLayout:
            size_hint_y: None
            height: dp(54)
            spacing: dp(4)
            padding: dp(4)
            NavButton:
                text: "Inicio"
                on_release: app.root.current = "home"
            NavButton:
                text: "Tipos"
                on_release: app.root.current = "types"
            NavButton:
                text: "Simular"
                on_release: app.root.current = "sim"
            NavButton:
                text: "Más"
                on_release: app.root.current = "about"

<SimulatorScreen>:
    name: "sim"
    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(16)
        canvas.before:
            Color:
                rgba: (0.02, 0.03, 0.08, 1)
            Rectangle:
                pos: self.pos
                size: self.size

        TitleLabel:
            text: "Simulador"

        BodyLabel:
            text: "Mueve la barra. Cuando la Luna se acerca al centro, aumenta el porcentaje de cobertura."
            size_hint_y: None

        Widget:
            size_hint_y: .2

        FloatLayout:
            size_hint_y: .85

            Label:
                text: "☀"
                font_size: "150sp"
                color: (1, .65, .05, 1)
                pos_hint: {"center_x": .5, "center_y": .5}

            Label:
                text: "●"
                font_size: "130sp"
                color: (.04, .05, .08, 1)
                pos_hint: {"center_x": root.moon_x, "center_y": .5}

        Label:
            text: "Cobertura aproximada: " + str(root.coverage) + "%"
            color: (1,1,1,1)
            font_size: "20sp"
            size_hint_y: None
            height: dp(35)

        Slider:
            min: 0
            max: 100
            value: 50
            on_value: root.update_sim(self.value)
            size_hint_y: None
            height: dp(46)

        Label:
            text: root.eclipse_label
            color: (1, .72, .02, 1)
            font_size: "19sp"
            bold: True
            size_hint_y: None
            height: dp(36)

        Button:
            text: "Seguridad al observar"
            size_hint_y: None
            height: dp(48)
            background_normal: ""
            background_color: (1, .55, .03, 1)
            color: (0.05, .05, .08, 1)
            on_release: app.root.current = "safety"

        BoxLayout:
            size_hint_y: None
            height: dp(54)
            spacing: dp(4)
            NavButton:
                text: "Inicio"
                on_release: app.root.current = "home"
            NavButton:
                text: "Tipos"
                on_release: app.root.current = "types"
            NavButton:
                text: "Simular"
                on_release: app.root.current = "sim"
            NavButton:
                text: "Más"
                on_release: app.root.current = "about"

<SafetyScreen>:
    name: "safety"
    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: (0.02, 0.03, 0.08, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(14)
                size_hint_y: None
                height: self.minimum_height

                TitleLabel:
                    text: "Observación segura"

                Card:
                    TitleLabel:
                        text: "✅ Sí"
                        font_size: "22sp"
                    BodyLabel:
                        text: "• Usa gafas certificadas para observación solar.\\n• Revisa que el filtro esté en buen estado.\\n• Usa métodos de proyección indirecta.\\n• Sigue instrucciones de profesores o expertos."

                Card:
                    TitleLabel:
                        text: "❌ No"
                        font_size: "22sp"
                    BodyLabel:
                        text: "• No mires directamente al Sol sin protección.\\n• No uses gafas de sol comunes.\\n• No uses cámaras, binoculares o telescopios sin filtro solar adecuado.\\n• No improvises filtros caseros."

                Button:
                    text: "Ir al quiz"
                    size_hint_y: None
                    height: dp(50)
                    background_normal: ""
                    background_color: (1, .55, .03, 1)
                    color: (0.05, .05, .08, 1)
                    on_release: app.root.current = "quiz"

        BoxLayout:
            size_hint_y: None
            height: dp(54)
            spacing: dp(4)
            padding: dp(4)
            NavButton:
                text: "Inicio"
                on_release: app.root.current = "home"
            NavButton:
                text: "Tipos"
                on_release: app.root.current = "types"
            NavButton:
                text: "Simular"
                on_release: app.root.current = "sim"
            NavButton:
                text: "Más"
                on_release: app.root.current = "about"

<QuizScreen>:
    name: "quiz"
    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(14)
        canvas.before:
            Color:
                rgba: (0.02, 0.03, 0.08, 1)
            Rectangle:
                pos: self.pos
                size: self.size

        TitleLabel:
            text: "Mini quiz"

        Label:
            text: root.question_text
            color: (1,1,1,1)
            font_size: "21sp"
            text_size: self.width, None
            halign: "left"
            valign: "middle"

        Button:
            text: root.answer_a
            on_release: root.answer(0)
        Button:
            text: root.answer_b
            on_release: root.answer(1)
        Button:
            text: root.answer_c
            on_release: root.answer(2)
        Button:
            text: root.answer_d
            on_release: root.answer(3)

        Label:
            text: root.feedback
            color: (1, .72, .02, 1)
            font_size: "17sp"
            text_size: self.width, None
            halign: "center"

        Button:
            text: "Siguiente"
            size_hint_y: None
            height: dp(48)
            background_normal: ""
            background_color: (1, .55, .03, 1)
            color: (0.05, .05, .08, 1)
            on_release: root.next_question()

        BoxLayout:
            size_hint_y: None
            height: dp(54)
            spacing: dp(4)
            NavButton:
                text: "Inicio"
                on_release: app.root.current = "home"
            NavButton:
                text: "Tipos"
                on_release: app.root.current = "types"
            NavButton:
                text: "Simular"
                on_release: app.root.current = "sim"
            NavButton:
                text: "Más"
                on_release: app.root.current = "about"

<AboutScreen>:
    name: "about"
    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: (0.02, 0.03, 0.08, 1)
            Rectangle:
                pos: self.pos
                size: self.size

        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(16)
                size_hint_y: None
                height: self.minimum_height

                TitleLabel:
                    text: "Acerca del proyecto"

                Card:
                    TitleLabel:
                        text: "Tecnologías"
                        font_size: "22sp"
                    BodyLabel:
                        text: "Aplicación desarrollada en Python usando Kivy. Puede compilarse como APK para Android."

                Card:
                    TitleLabel:
                        text: "Autor"
                        font_size: "22sp"
                    BodyLabel:
                        text: "Carlos Felipe Obando Latorre\\nCurso 10-2\\n2026"

                Button:
                    text: "Ir al quiz"
                    size_hint_y: None
                    height: dp(50)
                    background_normal: ""
                    background_color: (1, .55, .03, 1)
                    color: (0.05, .05, .08, 1)
                    on_release: app.root.current = "quiz"

        BoxLayout:
            size_hint_y: None
            height: dp(54)
            spacing: dp(4)
            padding: dp(4)
            NavButton:
                text: "Inicio"
                on_release: app.root.current = "home"
            NavButton:
                text: "Tipos"
                on_release: app.root.current = "types"
            NavButton:
                text: "Simular"
                on_release: app.root.current = "sim"
            NavButton:
                text: "Más"
                on_release: app.root.current = "about"
"""

class HomeScreen(Screen):
    pass

class TypesScreen(Screen):
    pass

class SimulatorScreen(Screen):
    moon_x = NumericProperty(0.5)
    coverage = NumericProperty(100)
    eclipse_label = StringProperty("Eclipse total")

    def update_sim(self, value):
        self.moon_x = 0.15 + (value / 100.0) * 0.70
        distance = abs(value - 50)
        self.coverage = max(0, round(100 - distance * 3.2))
        if self.coverage >= 92:
            self.eclipse_label = "Eclipse total"
        elif self.coverage >= 12:
            self.eclipse_label = "Eclipse parcial"
        else:
            self.eclipse_label = "Sin eclipse"

class SafetyScreen(Screen):
    pass

class QuizScreen(Screen):
    question_text = StringProperty("")
    answer_a = StringProperty("")
    answer_b = StringProperty("")
    answer_c = StringProperty("")
    answer_d = StringProperty("")
    feedback = StringProperty("Selecciona una respuesta.")

    questions = [
        ("¿Qué astro se coloca entre el Sol y la Tierra durante un eclipse solar?",
         ["Marte", "La Luna", "Venus", "Júpiter"], 1),
        ("¿Qué tipo de eclipse deja visible un anillo brillante?",
         ["Total", "Parcial", "Anular", "Lunar"], 2),
        ("¿Cuál es una forma segura de observar un eclipse?",
         ["Gafas de sol comunes", "Mirar unos segundos", "Filtro solar certificado", "Celular sin filtro"], 2),
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.score = 0
        self.answered = False
        self.load_question()

    def load_question(self):
        q, options, _ = self.questions[self.index]
        self.question_text = f"Pregunta {self.index + 1} de {len(self.questions)}\n\n{q}"
        self.answer_a, self.answer_b, self.answer_c, self.answer_d = options
        self.feedback = "Selecciona una respuesta."
        self.answered = False

    def answer(self, selected):
        if self.answered:
            return
        self.answered = True
        correct = self.questions[self.index][2]
        if selected == correct:
            self.score += 1
            self.feedback = "¡Correcto!"
        else:
            self.feedback = f"Incorrecto. Respuesta correcta: {self.questions[self.index][1][correct]}"

    def next_question(self):
        if not self.answered:
            self.feedback = "Primero selecciona una respuesta."
            return

        if self.index < len(self.questions) - 1:
            self.index += 1
            self.load_question()
        else:
            self.question_text = f"Resultado final\n\nObtuviste {self.score} de {len(self.questions)} respuestas correctas."
            self.answer_a = "Reiniciar quiz"
            self.answer_b = "-"
            self.answer_c = "-"
            self.answer_d = "-"
            self.feedback = "¡Quiz terminado!"
            self.index = -1
            self.answered = True

    def answer(self, selected):
        if self.index == -1:
            if selected == 0:
                self.index = 0
                self.score = 0
                self.load_question()
            return

        if self.answered:
            return

        self.answered = True
        correct = self.questions[self.index][2]
        if selected == correct:
            self.score += 1
            self.feedback = "¡Correcto!"
        else:
            self.feedback = f"Incorrecto. Respuesta correcta: {self.questions[self.index][1][correct]}"

class AboutScreen(Screen):
    pass

class EclipseLabApp(App):
    title = "EclipseLab"
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    EclipseLabApp().run()
