import tornado.ioloop
import tornado.web
from tornado import websocket
from chatterbot import ChatBot
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class ClientSocket(websocket.WebSocketHandler):
    def open(self):
        chatbot = ChatBot(
            'Captain Phasma',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )
        chatbot.train("chatterbot.corpus.english")
        self.chatbot = chatbot

    def on_message(self, message):
        self.write_message(self.chatbot.get_response(message).text)

    def on_close(self):
        pass


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/push", ClientSocket),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': os.curdir}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()