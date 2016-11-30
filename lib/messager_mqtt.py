#!/usr/bin/python
import time
import json
import logging


logger = logging.getLogger(__name__)

LOGLEVEL = 'DEBUG'



def  create_message(text,sender,id='0',area='0',bounce='0',time=time.time()):
    """
    Standard form for modules message structure
    :param text: Indata, the real message
    :param sender: Module name stt, tts chatbot etc
    :param id: Manage by Alpha main proc. initial 0 if stt module initiates message
    :param area: (livingroom, kithcen etc.)
    :param bounce: (how many time the message have bounced between modules
    :param time: Initial start time
    :return: json message object
    """
    logger.debug('create_message - initiate new message')
    message = json.dumps(
        {'text': text,'sender': sender, 'id': id, 'area': area, 'bounce': bounce, 'time': time})
    return message

def extract_message(json_obj,text=None,sender=None,id=None,area=None,bounce=None,time=None,topic=None):
    """
    This function extract a variable from json obj (module message)
    :param json_obj:
    :param text:
    :param sender:
    :param id:
    :param area:
    :param bounce:
    :param time:
    :param topic:
    :return:
    """
    logger.debug('extract_message - decode message to variables')
    decode = json.loads(json_obj)
    extracted_text = decode['text']
    extracted_sender = decode['sender']
    extracted_id = decode['id']
    extracted_area = decode['area']
    extracted_bounce = decode['bounce']
    extracted_time = decode['time']
    extracted_topic = json_obj
    # This is more of an example how json can be extract
    if text is None and sender is None and id is None and area is None and bounce is None and time is None:
    #if text is None and sender is None:
        logger.debug('extract_message - extract everything in message')
        # Might be a dict instead.
        return (extracted_text,extracted_sender,extracted_id,extracted_area,extracted_bounce,extracted_time)
        #return True
    if text is not None:
        return extracted_text
    if sender is not None:
        return extracted_sender
    if id is not None:
        return extracted_id
    if area is not None:
        return extracted_area
    if bounce is not None:
        return extracted_bounce
    if time is not None:
        return extracted_time
    if topic is not None:
        return extracted_topic


def create_from_message(json_obj,new_text,new_sender):
    """
    This function create/updates a json obj message to a new. Ex. a module updates information
    Could be that chatbot makes an assumption and message change its pattern.
    :param json_obj: created from create_message
    :param new_sender: (module name stt, tts, chatbot etc)
    :return: new json_obj
    """
    logger.debug('create_from_messages - create new and keep id,area and time from initial')
    #e_text = extract_message(json_obj,text)
    e_id = extract_message(json_obj, id='get')
    e_area = extract_message(json_obj, area='get')
    ''' e_bounce = extract_message(json_obj, bounce='get') '''
    ''' When a module enhance a message it apply to a new set of rules and relations, there for bounce becomes 0 '''
    e_bounce = '0'
    e_time = extract_message(json_obj, time='get')
    new_json_obj = create_message(new_text,new_sender,e_id,e_area,e_bounce,e_time)
    return new_json_obj

def bounche_message(json_obj):
    """
    When Alpha/main proc for example determ what happens next with a json message,
    it should bounce/add 1 jump step to the origin message, before sending it away to the
    next module.
    :param json_obj:
    :return: new updated original json message
    """

    e_text, e_sender, e_id, e_area, e_bounce, e_time = extract_message(json_obj)
    e_bounce = str(int(e_bounce) + 1)
    new_json_obj = create_message(e_text, e_sender, e_id, e_area, e_bounce, e_time)
    logger.debug('bounced_message - added 1 [\033[0;32%s\033[0m]',new_json_obj)
    return new_json_obj


if __name__ == '__main__':
    send_topic = yconfig['mqtt']['topic']['chatbot']
    listen_topic = yconfig['chatbot']['mqtttopic']
    numeric_level = getattr(logging, LOGLEVEL, None)
    FORMAT = '%(asctime)-15s %(levelname)s    - %(name)s - %(message)s'
    logging.basicConfig(format=FORMAT,level=numeric_level)
    logger = logging.getLogger('Chatbot')
    logger.debug('  main listen to mqtt topic [\033[0;32matarting\033[0m]')



