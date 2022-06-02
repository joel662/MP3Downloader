from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import youtube_dl


class MyGridLayout(GridLayout, Widget):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Enter URL "))
        self.link = TextInput(multiline=False)
        self.inside.add_widget(self.link)

        self.add_widget(self.inside)

        self.download = Button(text="Download", font_size=40)
        self.download.bind(on_press=self.get_mp3)
        self.add_widget(self.download)


    def get_mp3(self,instance):
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=self.link.text, download=False
        )

        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': f"{video_info['title']}.mp3",
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])


class myapp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    myapp().run()
