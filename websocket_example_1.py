from websocket import create_connection, WebSocket
import ssl

class MyWebSocket(WebSocket):
    def recv_message(self):
        message = super().recv_frame()
        print('Recieved message: {}'.format(message))
        return message



ws = create_connection("ws://0.0.0.0:8181/core", sslopt={"cert_reqs": ssl.CERT_NONE}, class_=MyWebSocket)
mycroft_question = 'what time is it'
mycroft_type = 'recognizer_loop:utterance'
mycroft_data = '{"utterances": ["%s"]}' % mycroft_question
message = '{"type": "' + mycroft_type + '", "data": ' + mycroft_data + '}'
print("Sending 'Message'...")
ws.send(message)
print(ws.recv())
print(ws.recv())
print("Sent")
