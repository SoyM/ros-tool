from __future__ import print_function

import time


from roslibpy import Message, Ros, Topic


def run_topic_pubsub():
    context = {'counter': 0}
    ros_client = Ros('192.168.1.106', 9090)
    listener = Topic(ros_client, '/chatter', 'std_msgs/String')
    publisher = Topic(ros_client, '/chatter', 'std_msgs/String')

    def receive_message(message):
 
        print("============================")
        context['counter'] += 1
        assert message['data'] == 'hello world', 'Unexpected message content'

        if context['counter'] == 3:
            listener.unsubscribe()
            # Give it a bit of time, just to make sure that unsubscribe
            # really unsubscribed and counter stays at the asserted value
            ros_client.call_later(2, ros_client.terminate)
	
    # def callback(topic_list):
    #     print(topic_list)
    #     assert('/rosout' in topic_list['topics'])
    #     time.sleep(1)
    #     ros_client.terminate()

    def start_sending():
        while True:
            print("---------------------")
            if not ros_client.is_connected:
                break
            publisher.publish(Message({'data': 'hello world'}))
            print(listener.is_subscribed)

            time.sleep(0.1)
            ros_client.terminate
            break
            # ros_client.get_topics(callback)

        publisher.unadvertise()

    def start_receiving():
        listener.subscribe(receive_message)

    ros_client.on_ready(start_receiving, run_in_thread=True)
    ros_client.on_ready(start_sending, run_in_thread=True)
    
    ros_client.run_forever()

    assert context['counter'] >= 3, 'Expected at least 3 messages but got ' + str(context['counter'])




if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG, format='[%(thread)03d] %(asctime)-15s [%(levelname)s] %(message)s')
    LOGGER = logging.getLogger('test')

    run_topic_pubsub()
