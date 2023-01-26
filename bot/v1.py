import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import cryptocode
vk_session = vk_api.VkApi(token = "vk1.a.HsbWVFW6rhyO5JARvzXaOSLyLahKbUoDr72iaEj4hzt_3nG8bAhr9z4y4wU7UQtZTYX9vQzZtaJRjdnQXRfsjyH-tHCawTnAWyfFjvMI-KkqhOa3gMYKsRds6MntqCthtdmdkf5WTEovnWUNrNvR3gVULeP0gFivPL9ad3T7wET9OhizBgpPXZseJMl5-2QcJ4ExwJzlLGP6zAn8BylD1A")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 218402290)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer_id = event.object.message['peer_id']
        from_id = event.object.message['from_id']
        mtext = event.object.message['text']
        m = str(mtext)
        s = m.split()
        c = s[0]
        w = s[1]
        k = s[2]
        encode = cryptocode.encrypt(w, k)
        decode = cryptocode.decrypt(w, k)
        if peer_id != from_id:
            if c == 'Ш':
                vk.messages.send(peer_id=peer_id, message=f"{encode}", random_id=0)
            elif c == 'Р':
                vk.messages.send(peer_id=peer_id, message=f"{decode}", random_id=0)
        elif peer_id == from_id or peer_id <= from_id or peer_id >= from_id:
            if c == 'Р':
                vk.messages.send(peer_id=peer_id, message=f"{decode}", random_id=0)
            elif c == 'Ш':
                vk.messages.send(peer_id=peer_id, message=f"{encode}", random_id=0)
