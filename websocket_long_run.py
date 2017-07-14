#!/usr/bin/python
import websocket
import _thread
import time
import json

def on_message(ws, message):
    output = json.loads(message)
    print(output)
    if output['data']['expect_response'] == False:
        print(output['data']['utterance'])
    else:
        pass

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        time.sleep(1)
        mycroft_question = 'what time is it'
        mycroft_type = 'recognizer_loop:utterance'
        mycroft_data = '{"utterances": ["%s"]}' % mycroft_question
        message = '{"type": "' + mycroft_type + '", "data": ' + mycroft_data + '}'
        ws.send(message)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())



if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://0.0.0.0:8181/core",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()
