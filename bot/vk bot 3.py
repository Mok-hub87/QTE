import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
vk_session = vk_api.VkApi(token = "vk1.a.HsbWVFW6rhyO5JARvzXaOSLyLahKbUoDr72iaEj4hzt_3nG8bAhr9z4y4wU7UQtZTYX9vQzZtaJRjdnQXRfsjyH-tHCawTnAWyfFjvMI-KkqhOa3gMYKsRds6MntqCthtdmdkf5WTEovnWUNrNvR3gVULeP0gFivPL9ad3T7wET9OhizBgpPXZseJMl5-2QcJ4ExwJzlLGP6zAn8BylD1A")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 218402290)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer_id = event.object.message['peer_id']
        from_id = event.object.message['from_id']
        mtext = event.object.message['text']
        if peer_id != from_id:
            m = str(mtext)
            vk.messages.send(peer_id = peer_id, message = f"{mtext}", random_id = 0)
        else:
            vk.messages.send(peer_id=peer_id, message=f"{mtext}", random_id=0)
